from setuptools import setup, find_packages

setup(
    name='cmlidar',
    version='v0.1.1',
    packages=find_packages(),
    install_requires=['matplotlib', 'numpy'],
    package_data={
        'cmlidar': ['rgb/*.csv',],
    },
)