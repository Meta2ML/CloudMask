<div align="center">

[![logo](https://raw.githubusercontent.com/XavierJiezou/CloudMask/main/images/favicon_256x256.svg)](https://pixelied.com/editor/design/6282f5970515730397249959)

# Cloud Mask

Cloud Mask with Landsat 8 and Sentinel 2.

<p>
    <a href="https://github.com/XavierJiezou/CloudMask/actions?query=workflow:Release">
        <img src="https://github.com/XavierJiezou/CloudMask/workflows/Release/badge.svg"
            alt="GitHub Workflow Release Status" />
    </a>
    <a href="https://github.com/XavierJiezou/CloudMask/actions?query=workflow:Test">
        <img src="https://github.com/XavierJiezou/CloudMask/workflows/Test/badge.svg"
            alt="GitHub Workflow Test Status" />
    </a>
    <a href="https://github.com/XavierJiezou/CloudMask/actions?query=workflow:Lint">
        <img src="https://github.com/XavierJiezou/CloudMask/workflows/Lint/badge.svg"
            alt="GitHub Workflow Lint Status" />
    </a>
    <a href='https://cloudmask.readthedocs.io/en/latest/?badge=latest'>
        <img src='https://readthedocs.org/projects/cloudmask/badge/?version=latest' alt='Documentation Status' />
    </a>
    <a
        href="https://www.codacy.com/gh/XavierJiezou/CloudMask/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=XavierJiezou/CloudMask&amp;utm_campaign=Badge_Grade">
        <img src="https://app.codacy.com/project/badge/Grade/c2f85c8d6b8a4892b40059703f087eab" alt="Codacy Badge">
    </a>
    <a href="https://codecov.io/gh/XavierJiezou/CloudMask">
        <img src="https://codecov.io/gh/XavierJiezou/CloudMask/branch/main/graph/badge.svg?token=QpCLcUGoYx"
            alt="codecov">
    </a>
    <a href="https://pypi.org/project/cloudmask/">
        <img src="https://img.shields.io/pypi/v/CloudMask" alt="PyPI">
    </a>
    <a href="https://pypistats.org/packages/cloudmask">
        <img src="https://img.shields.io/pypi/dm/CloudMask" alt="PyPI - Downloads">
    </a>
    <!-- <a href="https://pypi.org/project/cloudmask/">
        <img src="https://img.shields.io/pypi/pyversions/CloudMask" alt="PyPI - Python Version">
    </a> -->
    <a href="https://github.com/XavierJiezou/CloudMask/stargazers">
        <img src="https://img.shields.io/github/stars/XavierJiezou/CloudMask" alt="GitHub stars">
    </a>
    <a href="https://github.com/XavierJiezou/CloudMask/network">
        <img src="https://img.shields.io/github/forks/XavierJiezou/CloudMask" alt="GitHub forks">
    </a>
    <a href="https://github.com/XavierJiezou/CloudMask/issues">
        <img src="https://img.shields.io/github/issues/XavierJiezou/CloudMask" alt="GitHub issues">
    </a>
    <a href="https://github.com/XavierJiezou/CloudMask/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/XavierJiezou/CloudMask" alt="GitHub license">
    </a>
    <!-- <a href="https://github.com/psf/black">
        <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg" />
    </a> -->
</p>

<p>
    <!-- <a href="https://www.python.org/">
        <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" alt="forthebadge made-with-python">
    </a>
    <a href="https://github.com/XavierJiezou">
        <img src="http://ForTheBadge.com/images/badges/built-with-love.svg" alt="ForTheBadge built-with-love">
    </a> -->
    <a href="https://www.python.org/">
        <img alt="Python" src="https://img.shields.io/badge/-Python 3.7+-blue?style=for-the-badge&logo=python&logoColor=white"></a>
    <a href="https://pytorch.org/get-started/locally/">
        <img alt="PyTorch" src="https://img.shields.io/badge/-PyTorch 1.8+-ee4c2c?style=for-the-badge&logo=pytorch&logoColor=white"></a>
    <a href="https://pytorchlightning.ai/">
        <img alt="Lightning" src="https://img.shields.io/badge/-Lightning 1.5+-792ee5?style=for-the-badge&logo=pytorchlightning&logoColor=white">
    </a>
    <a href="https://hydra.cc/">
        <img alt="Config: hydra" src="https://img.shields.io/badge/config-hydra 1.1-89b8cd?style=for-the-badge&labelColor=gray"></a>
    <a href="https://black.readthedocs.io/en/stable/">
        <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-black.svg?style=for-the-badge&labelColor=gray">
    </a>
</p>

<p>
    <a href="#demo">View Demo</a>
    •
    <a href="https://github.com/XavierJiezou/CloudMask/issues/new">Report Bug</a>
    •
    <a href="https://github.com/XavierJiezou/CloudMask/issues/new">Request Feature</a>
</p>

<p>
    <a href="/docs/README.en.md">English </a>
    •
    <a href="/docs/README.cn.md">简体中文</a>
</p>

Love the project? Please consider [donating](https://paypal.me/xavierjiezou?country.x=C2&locale.x=zh_XC) to help it improve!

</div>

## Demo

![demo](https://raw.githubusercontent.com/XavierJiezou/CloudMask/main/images/favicon_256x256.svg)

## Features

- [ ] Cloud mask with Landsat 8.
- [ ] Cloud mask with Sentinel 2.

## Install

```bash
pip install cloudmask
```

## Usage

`$ cloudmask`

## Data

### Landasat 8

1. Download Landasat 8 data

```bash
python cloudmask/utils/download_landsat8.py
```

![download_landsat8](/images/download_landsat8.png)

2. Decompression

### Sentinel 2

## Changelog

See [CHANGELOG.md](/CHANGELOG.md)

## License

[MIT License](/LICENSE)

## Dependencies

### Production Dependencies

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=psf&repo=requests)](https://github.com/psf/requests)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=Textualize&repo=rich)](https://github.com/Textualize/rich)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=google&repo=python-fire)](https://github.com/google/python-fire)

### Development dependencies

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=python-poetry&repo=poetry)](https://github.com/python-poetry/poetry)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=pytest-dev&repo=pytest)](https://github.com/pytest-dev/pytest)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=pytest-dev&repo=pytest-cov)](https://github.com/pytest-dev/pytest-cov)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=pre-commit&repo=pre-commit)](https://github.com/pre-commit/pre-commit)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=PyCQA&repo=flake8)](https://github.com/PyCQA/flake8)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=PyCQA&repo=pylint)](https://github.com/PyCQA/pylint)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=psf&repo=black)](https://github.com/psf/black)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=uiri&repo=toml)](https://github.com/uiri/toml)
