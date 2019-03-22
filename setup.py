#!/usr/bin/python

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    name="easylogconfig",
    version="0.1.1",
    description="Easy configure logging",
    url="https://github.com/tierpod/easylogconfig",
    author="Pavel Podkorytov",
    author_email="pod.pavel@gmail.com",
    license='MIT',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
)
