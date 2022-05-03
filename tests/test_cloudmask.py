from cloudmask import __version__
import toml


def test_version():
    version = toml.load('pyproject.toml')['tool']['poetry']['version']
    assert version == __version__
