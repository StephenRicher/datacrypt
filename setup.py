#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Setup file for datavault. """


import os
import sys
import glob
from shutil import rmtree
from setuptools import setup, find_namespace_packages, Command


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


def get_info():
    info = {}
    versionPath = glob.glob('src/*/_version.py')[0]
    with open(versionPath) as fp:
        exec(fp.read(), info)
    return info


setup(
    name='datavault',
    author='Stephen Richer',
    author_email='stephen.richer@nhs.net',
    url='https://github.com/StephenRicher/datavault',
    entry_points={
        'console_scripts': ['datavault=datavault.parseArgs:parseArgs']
    },
    python_requires='>=3.8.0',
    install_requires=[
        'pandas',
        'cryptography',
    ],
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python :: 3',
        'Natural Language :: English',
    ],
    version=get_info()['__version__'],
    description=__doc__,
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    packages=find_namespace_packages(where='src'),
    package_dir={'': 'src'},
    zip_safe=False,
)
