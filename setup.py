from setuptools import setup, find_packages
import sys,os

setup(name='motmot.fview_show_geom',
      description='show geom targets on fview window and publish over ROS',
      version='0.0.1',
      packages = find_packages(),
      author='Dorothea Hoermann',
      author_email='john.stowers@gmail.com',
      entry_points = {
    'motmot.fview.plugins':'fview_show_geom = motmot.fview_show_geom.fview_show_geom:FviewShowGeom',
    },
      )
