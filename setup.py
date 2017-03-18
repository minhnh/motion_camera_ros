#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['motion_camera_ros'],
    package_dir={'motion_camera_ros': 'ros/src/motion_camera_ros'}
)

setup(**d)

