#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    find_packages,
    setup,
)

extras_require = {
    'dev': [
        "bumpversion",
        "flake8==3.4.1",
        "setuptools>=36.2.0",
        "twine",
    ]
}

setup(
    name='eth-dev',
    # *IMPORTANT*: Don't manually change the version here. Use the 'bumpversion' utility.
    version='0.1.0-alpha.3',
    description="""Ethereum Development Environment""",
    #long_description_markdown_filename='README.md',
    author='Bryant Eisenbach',
    author_email='fubuloubu@gmail.com',
    url='https://github.com/fubuloubu/eth-dev',
    include_package_data=True,
    install_requires=[
        "eth-account>=0.2.1,<0.4.0",
        "web3==5.0.0a3",  # TODO issue with >a3 installing 'eth-tester'
        "IPython",
    ],
    #setup_requires=['setuptools-markdown'],
    python_requires='>=3.6,<4',
    extras_require=extras_require,
    py_modules=['eth_dev'],
    scripts=[
        'scripts/eth-dev',
    ],
    license="MIT",
    zip_safe=False,
    keywords='ethereum',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
