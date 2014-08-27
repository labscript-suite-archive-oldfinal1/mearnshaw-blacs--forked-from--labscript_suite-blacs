from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
setup(
        name = "blacs",
        packages = find_packages(),
        include_package_data = True,
        install_requires = ['h5py', 'zprocess', 'qtutils']
)

