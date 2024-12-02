#!/usr/bin/env python
# (C) Copyright 2023 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#


import io
import os

import setuptools


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return io.open(file_path, encoding="utf-8").read()


version = None
for line in read("ai_models_graphcast/__init__.py").split("\n"):
    if line.startswith("__version__"):
        version = line.split("=")[-1].strip()[1:-1]


assert version


setuptools.setup(
    name="ai-models-graphcast",
    version=version,
    description="Run graphcast ai weather models",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="European Centre for Medium-Range Weather Forecasts (ECMWF)",
    author_email="software.support@ecmwf.int",
    license="Apache License Version 2.0",
    url="https://github.com/ecmwf-lab/ai-models-graphcast",
    packages=setuptools.find_packages(),
    include_package_data=True,
    # JAX requirements are in requirements.txt
    install_requires=[
        "ai-models>=0.4.0",
        "dm-tree",
        "dm-haiku==0.0.10",
    ],
    zip_safe=True,
    keywords="tool",
    entry_points={
        "ai_models.model": [
            "graphcast = ai_models_graphcast.model:model",
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
    ],
)
