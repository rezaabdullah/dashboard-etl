from setuptools import setup, find_packages

setup(
    name='dashboard-etl',
    version='1.0.0',
    packages=find_packages(include=['exampleproject', 'exampleproject.*'])
)