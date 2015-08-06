from __future__ import print_function
from glob import glob
from setuptools import setup, find_packages, Extension

sources = ['c/droidtools_ext4fsmodule.c']
sources.extend(glob("c/ext4_utils/*c"))
module_ext4 = Extension('droidtools.ext4fs',
                    define_macros = [('ANDROID', None)],
                    sources = sources,
                    libraries = ['z'],
                    include_dirs = [
                      'c/ext4_utils'
                      ]
                    )
setup(
    name='droidtools',
    packages= find_packages(),
    version="0.1",
    license='GPLv3 License',
    author='Tarek Galal',
    ext_modules = [module_ext4],
    author_email='tare2.galal@gmail.com',
    description='Some android tools',
    platforms='any'
)