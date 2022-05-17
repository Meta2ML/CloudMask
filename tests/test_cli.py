from __future__ import annotations

import toml

from cloudmask.cli import CloudMaskCli


class TestCloudMaskCli(CloudMaskCli):
    def test_version(self):
        version = toml.load("pyproject.toml")["tool"]["poetry"]["version"]
        assert version == self.version
