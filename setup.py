#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = []

test_requirements = []

setup(
    author="Kestin Goforth",
    author_email="kgoforth1503@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Generate various purge lines for your 3d printer nozzles.",
    entry_points={
        "console_scripts": [
            "purge_line_generator=purge_line_generator.cli:main",
        ],
    },
    install_requires=requirements,
    license="GNU Affero General Public License v3 or later",
    long_description=readme,
    include_package_data=True,
    keywords="purge_line_generator",
    name="purge_line_generator",
    packages=find_packages(include=["purge_line_generator", "purge_line_generator.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/kforth/purge_line_generator",
    version="0.1.0",
    zip_safe=False,
)
