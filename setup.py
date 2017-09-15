#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os


setup(
    name='pygments-style-balanced',
    version= '0.5',
    description='Pygments version of the Balanced theme.',
    packages=find_packages(),
    install_requires=['pygments >= 1.5'],
    entry_points="""
        [pygments.styles]
        balanced-dark=pygments_style_balanced_dark:BalancedDarkStyle
    """,
    zip_safe=False,
)