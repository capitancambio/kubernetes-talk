#!/usr/bin/env python
# -*- coding: utf-8 -*
import pathlib

from setuptools import find_packages, setup

VERSION = "0.0.1.dev0"

REPO_ROOT = pathlib.Path(__file__).parent

with open(REPO_ROOT / "README.md", encoding="utf-8") as f:
    README = f.read()


setup_args = dict(
    # Description
    name="scripts",
    version=VERSION,
    description="Example scripts for the kubernetes talk",
    long_description=README,
    # Credentials
    author="Javier Asensio Cubero",
    author_email="javier.asensio@octoenergy.com",
    url="https://github.com/capitancambio/kubernetes-talk",
    license="Beer license",
    # Package data
    package_dir={"": "src"},
    packages=find_packages("src", include=["*scripts*"]),
    zip_safe=False,
    entry_points={"console_scripts": ["scripts=scripts.transform:main"]},
)


if __name__ == "__main__":

    # Make install
    setup(**setup_args)
