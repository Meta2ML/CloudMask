from __future__ import annotations

import fire

from cloudmask import __version__


class CloudMaskCli:
    @property
    def version(self) -> str:
        return __version__


def main() -> None:
    fire.Fire(CloudMaskCli)


if __name__ == "__main__":
    main()
