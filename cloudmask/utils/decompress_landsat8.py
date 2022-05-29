import glob
import os
import tarfile
from typing import List

import gevent
from gevent.threadpool import ThreadPool
from rich.live import Live
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    DownloadColumn,
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
        desc = f"[magenta]Extracting... [cyan]{scene}"
        with self.job_progress.open(scene, "rb", description=desc) as file:
            tar = tarfile.open(fileobj=file)
            tar.extractall(self.root)
            tar.close()
        self.overall_progress.update(self.overall_task, advance=1)

    def get_scenes(self) -> List[str]:
        pathname = os.path.join(self.root, "*/*")
        return glob.glob(pathname)

    def show(self) -> Table:
        self.overall_progress = Progress(
            SpinnerColumn(),
            "{task.description}",
            BarColumn(),
            "[green]{task.completed}/{task.total}",
            TaskProgressColumn(),
            TimeElapsedColumn(),
            TimeRemainingColumn(),
        )
        self.job_progress = Progress(
            SpinnerColumn(),
            "{task.description}",
            BarColumn(),
            DownloadColumn(),
            TaskProgressColumn(),
            TimeElapsedColumn(),
            TimeRemainingColumn(),
            transient=True,
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

    def main(self, max_workers: int = 12) -> None:
        scenes = self.get_scenes()
        progress_table = self.show()
        self.overall_task = self.overall_progress.add_task(
            description=f"[green]Decompress [magenta]{self.name}[/magenta] to [cyan]{self.root}",
            total=len(scenes),
        )
        with Live(progress_table, refresh_per_second=10):
            pool = ThreadPool(max_workers)
            for scene in scenes:
                pool.spawn(self.decompress_scene, scene)
            gevent.wait()


if __name__ == "__main__":
    DecompressLandsat8()
