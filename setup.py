from setuptools import setup, find_packages

setup(
    name='infernyx',
    version='0.1',
    packages=['infernyx'],
    url='',
    license='',
    author='tspurway',
    author_email='tspurway@mozilla.com',
    description='Inferno rules for Tiles Project',
    requires=['inferno', 'boto', 'geoip2']
)
