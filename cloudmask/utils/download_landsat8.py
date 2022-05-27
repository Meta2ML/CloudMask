from gevent import monkey, pool  # isort:skip

monkey.patch_all()  # isort:skip

import os
import re
from typing import Dict, List

import requests
from rich.live import Live
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)
from rich.table import Table


class DownloadLandsat8:
    def __init__(self, root: str = "data/landsat8") -> None:
        self.name = "Landsat 8 Cloud Cover Assessment Validation Data"
        self.site = (
            "https://landsat.usgs.gov/landsat-8-cloud-cover-assessment-validation-data"
        )
        self.root = root
        self.main()

    def download_scene(self, url: str, type: str) -> None:
        res = requests.get(url, stream=True)
        name = os.path.basename(url)
        path = os.path.join(self.root, type, name)
        with open(path, "wb") as f:
            job = self.job_progress.add_task(
                description=f"[magenta]{type} [cyan]{path}",
                total=int(res.headers.get("Content-Length")) // (2**20) + 1,
            )
            for i in res.iter_content(int(2**20)):
                f.write(i)
                self.job_progress.update(job, advance=1)
        self.overall_progress.update(self.overall_task, advance=1)

    def get_scenes(self) -> List[Dict[str, str]]:
        res = requests.get(self.site)
        scene_url = re.findall("https://.*?.tar.gz", res.text)
        scene_class = [
            "Barren",
            "Forest",
            "Grass|Crops",
            "Shrubland",
            "Snow|Ice",
            "Urban",
            "Water",
            "Wetlands",
        ]
        for i in scene_class:
            os.makedirs(os.path.join(self.root, i), exist_ok=True)
        scenes = []
        for idx, url in enumerate(scene_url):
            scenes.append(
                {
                    "url": url,
                    "type": scene_class[idx // 12],
                }
            )
        return scenes

    def show(self) -> Table:
        self.overall_progress = Progress(
            SpinnerColumn(),
            "{task.description}",
            "[green]{task.completed}/{task.total}",
            BarColumn(),
            TaskProgressColumn(),
            TimeElapsedColumn(),
            TimeRemainingColumn(),
        )
        self.job_progress = Progress(
            SpinnerColumn(),
            "{task.description}",
            "[green]{task.completed}/{task.total} MB",
            BarColumn(),
            TaskProgressColumn(),
            TimeElapsedColumn(),
            TimeRemainingColumn(),
        )
        progress_table = Table.grid()
        progress_table.add_row(
            Panel(
                self.overall_progress,
                title="Overall",
                border_style="green",
                padding=(1, 1),
            ),
        )
        progress_table.add_row(
            Panel(self.job_progress, title="Jobs", border_style="red", padding=(1, 1)),
        )
        return progress_table

    def main(self, num_coroutine: int = 12) -> None:
        scenes = self.get_scenes()

        progress_table = self.show()

        self.overall_task = self.overall_progress.add_task(
            description=f"[green]Download [magenta][link={self.site}]{self.name}[/link][/magenta] to [cyan]{self.root}",
            total=len(scenes),
        )

        coroutine_pool = pool.Pool(num_coroutine)

        with Live(progress_table):
            for item in scenes:
                coroutine_pool.spawn(self.download_scene, item["url"], item["type"])
            coroutine_pool.join()


if __name__ == "__main__":
    DownloadLandsat8()
