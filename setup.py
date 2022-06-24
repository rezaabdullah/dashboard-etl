from setuptools import setup, find_packages

# setup(
#     name='example',
#     version='0.1.0',
#     packages=find_packages(include=['exampleproject', 'exampleproject.*']),
#     install_requires=[
#         'PyYAML',
#         'pandas==0.23.3',
#         'numpy>=1.14.5',
#         'matplotlib>=2.2.0',
#         'jupyter'
#     ]
# )

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name="dashboard-etl",
    version="1.0.0",
    author="Abdullah Reza",
    description="ETL project for Google Data Studio Dashboard",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rezaabdullah/dashboard-etl",
    keywords=["etl, data visualization, analytics, dashboard"],
    license = "Apache License 2.0",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    python_requires=">=3.8",
    install_requires=["pandas >= 1.3.0",
        "SQLAlchemy >= 1.4.30",
        "python-dotenv >= 0.19.0"],
    extras_require={
        "interactive": ["jupyter >= 1.0.0", "seaborn"],
        "dev": ["flake8 >= 4.0.1", "black >= 22.3.0"]
    },
    # package_data={
    #     'sample': ['example_data.csv'],
    # },
    entry_points={
        "console_scripts": [
            "etl = etl.__main__:main"
        ]
    }
)