#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020  The SymbiFlow Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier:	ISC

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="stdm",
    version="0.1",
    author="SymbiFlow Authors",
    author_email="symbiflow@lists.librecores.org",
    description="SymbiFlow Tools Data Manager",
    python_requires=">=3.6",
    url="https://github.com/SymbiFlow/symbiflow-tools-data-manager.git",
    entry_points={
        "console_scripts": ["symbiflow_get_latest_artifact_url=stdm.__init__:main"]
    },
    install_requires=[
        "requests",
    ],
    license="ISC",
    long_description=read("README.md"),
    packages=["stdm"],
)
