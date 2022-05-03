from cloudmask.cli import CloudMaskCLI
import toml


class TestCloudMaskCLI(CloudMaskCLI):
    def test_version(self):
        version = toml.load('pyproject.toml')['tool']['poetry']['version']
        assert version == self.version()
