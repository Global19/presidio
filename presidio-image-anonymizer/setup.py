"""Setup.py for Presidio Image Analyzer and Anonymizer."""
import os.path
from os import path

from setuptools import setup, find_packages

requirements = ["pillow", "pytesseract==0.3.7", "presidio-analyzer>=1.9.0"]

test_requirements = ["pytest>=3", "flake8==3.7.9"]

this_directory = path.abspath(path.dirname(__file__))
parent_directory = os.path.abspath(os.path.join(this_directory, os.pardir))

with open(path.join(this_directory, 'README.MD'), encoding='utf-8') as f:
    long_description = f.read()

with open(os.path.join(parent_directory, "VERSION")) as version_file:
    __version__ = version_file.read().strip()

setup(
    name="presidio_image_anonymizer",
    version=__version__,
    description="Presidio image anonymizer package",
    url="https://github.com/Microsoft/presidio",
    packages=find_packages(exclude=["tests"]),
    test_suite="tests",
    trusted_host=["pypi.org"],
    tests_require=test_requirements,
    install_requires=requirements,
    include_package_data=True,
    license="MIT",
keywords="presidio_image_anonymizer",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
