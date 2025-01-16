from setuptools import setup, find_packages

setup(
    name='cmlidar',
    version='v1.0.0',
    packages=find_packages(),
    install_requires=['matplotlib', 'numpy'],
    package_data={
        'cmlidar': ['rgb/*.csv',],
    },
)