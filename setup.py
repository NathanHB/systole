# Copyright (C) 2019 Nicolas Legrand
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


DESCRIPTION = """Psychophysiology with Python"""

DISTNAME = "systole"
MAINTAINER = "Nicolas Legrand"
MAINTAINER_EMAIL = "nicolas.legrand@cfin.au.dk"
VERSION = "0.1.3"

INSTALL_REQUIRES = [
    "numpy>=1.16",
    "scipy>=1.2",
    "pandas>=0.24",
    "matplotlib>=3.0.2",
    "seaborn>=0.9.0",
    "pyserial>=3.4",
    "py-ecg-detectors==1.0.2",
]

PACKAGES = ["systole", "systole.datasets"]

try:
    from setuptools import setup

    _has_setuptools = True
except ImportError:
    from distutils.core import setup

if __name__ == "__main__":

    setup(
        name=DISTNAME,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=open("README.rst").read(),
        long_description_content_type="text/x-rst",
        license="GPL-3.0",
        version=VERSION,
        install_requires=INSTALL_REQUIRES,
        include_package_data=True,
        packages=PACKAGES,
    )
