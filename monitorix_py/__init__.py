"""
Monitorix-py - A Python3 rewrite of Monitorix system monitoring tool.

This package provides a lightweight system monitoring solution designed to
monitor as many services and system resources as possible.

Original Monitorix project: https://github.com/mikaku/Monitorix
Copyright (C) 2005-2022 by Jordi Sanfeliu <jordi@fibranet.cat>

This Python3 rewrite is licensed under the GNU General Public License v2.
"""

__version__ = "0.1.0"
__author__ = "Monitorix Python Port Team"

from .monitorix import main

__all__ = ["main"]
