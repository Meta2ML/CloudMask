from scripts.multi_thread_downloader import Downloader
from tqdm import tqdm
import requests
import re
import os


def download(url):
    res = requests.get(url)
    scenes_list = re.findall(r'https://landsat.usgs.gov/cloud-validation/cca_l8/.*?.tar.gz', res.text)
    for scene_url in tqdm(scenes_list):
        Downloader(scene_url, f'data/{os.path.basename(scene_url)}').main()


if __name__ == '__main__':
    download('https://landsat.usgs.gov/landsat-8-cloud-cover-assessment-validation-data')
