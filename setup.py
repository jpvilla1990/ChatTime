from setuptools import setup, find_packages

setup(
    name='ChatTime',
    version='0.1',
    packages=find_packages(where='.'),  # Look for packages in the current directory (ChatTime)
    package_dir={'': '.'},  # Treat the current directory (ChatTime) as the root package
)
