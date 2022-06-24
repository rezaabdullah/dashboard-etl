# from setuptools import setup, find_packages

# setup(
#     name='dashboard-etl',
#     version='1.0.0',
#     packages=find_packages(include=['exampleproject', 'exampleproject.*'])
# )

from setuptools import setup

if __name__ == '__main__':
    setup()

# setup(
#     name="dashboard-etl"
#     version="1.0.0",
#     author="Abdullah Reza",
#     description="ETL project for Google Data Studio Dashboard",
#     long_description='This is a longer description for the project',
#     url='https://medium.com/@gmyrianthous',
#     keywords='sample, example, setuptools',
#     python_requires='>=3.7, <4',
#     install_requires=['pandas'],
#     extras_require={
#         'test': ['pytest', 'coverage'],
#     },
#     package_data={
#         'sample': ['example_data.csv'],
#     },
#     entry_points={
#         'runners': [
#             'sample=sample:main',
#         ]
#     }
# )