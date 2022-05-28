from gevent import monkey, pool  # isort:skip

monkey.patch_all()  # isort:skip

import glob
import os
import tarfile
from typing import List

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


class DecompressLandsat8:
    def __init__(self, root: str = "data/landsat8") -> None:
        self.name = "Landsat 8 Cloud Cover Assessment Validation Data"
        self.root = root
        self.main()

    def decompress_scene(self, scene: str) -> None:
        tar = tarfile.open(scene)
        members = tar.getmembers()
        job = self.job_progress.add_task(
            description=f"[magenta]Extracting [cyan]{scene}",
            total=len(members),
        )
        for member in members:
            tar.extract(member, self.root)
            self.job_progress.update(job, advance=1)
        tar.close()
        self.overall_progress.update(self.overall_task, advance=1)

    def get_scenes(self) -> List[str]:
        pathname = os.path.join(self.root, "*/*")
        return glob.glob(pathname)

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
            description=f"[green]Decompress [magenta]{self.name}[/magenta] to [cyan]{self.root}",
            total=len(scenes),
        )
        coroutine_pool = pool.Pool(num_coroutine)
        with Live(progress_table):
            for scene in scenes:
                coroutine_pool.spawn(self.decompress_scene, scene)
            coroutine_pool.join()


if __name__ == "__main__":
    DecompressLandsat8()
