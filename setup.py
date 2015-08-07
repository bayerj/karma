#! /usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Justin Bayer, bayer.justin@googlemail.com'


from setuptools import setup, find_packages


setup(
    name="karma",
    version="pre-0.1",
    description="reinforcement learning",
    license="BSD",
    keywords="reinforcement learning",
    packages=find_packages(exclude=['examples', 'docs']),
    include_package_data=True,
)

