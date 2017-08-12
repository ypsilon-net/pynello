import os
from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='pynello',
    version='1.3',
    license='GPL3',
    description='Python library for nello.io intercoms',
    long_description=read('README.rst'),
    author='Philipp Schmitt',
    author_email='philipp@schmitt.co',
    url='https://github.com/pschmitt/pynello',
    packages=find_packages(),
    install_requires=['python-dateutil', 'requests'],
    entry_points={'console_scripts': ['nello=pynello.__main__:main']}
)
