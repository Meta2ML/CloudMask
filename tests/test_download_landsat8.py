from cloudmask.utils import download_landsat8


def test_download_landsat8():
    assert len(download_landsat8()) == 96
