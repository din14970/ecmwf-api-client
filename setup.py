#!/usr/bin/env python
#
# (C) Copyright 2012-2019 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0. 
# In applying this licence, ECMWF does not waive the privileges and immunities 
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.
#

import io
import os

from setuptools import setup, find_packages

import ecmwfapi


def read(path):
    file_path = os.path.join(os.path.dirname(__file__), *path.split('/'))
    return io.open(file_path, encoding='utf-8').read()


setup(
    name="ecmwf-api-client",
    version=ecmwfapi.__version__,
    description=ecmwfapi.__doc__,
    long_description=read('README.md'),
    author="ECMWF",
    author_email="software.support@ecmwf.int",
    license='Apache License Version 2.0',
    url="https://github.com/ecmwf/ecmwf-api-client",

    # entry_points={
    #     "console_scripts": [
    #         "mars = XXX:main",
    #     ],
    # },

    packages=find_packages(),
    zip_safe=False,
)
