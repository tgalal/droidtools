from __future__ import print_function
from glob import glob
from setuptools import setup, find_packages, Extension

sources = ['c/droidtools_ext4fsmodule.c']
sources.extend(glob("c/ext4_utils/*.c"))
module_ext4 = Extension('droidtools.ext4fs',
                    define_macros = [('ANDROID', None)],
                    sources = sources,
                    libraries = ['z'],
                    include_dirs = [
                      'c/ext4_utils',
                      'c/ext4_utils/private'
                      ]
                    )
setup(
    name='droidtools',
    packages= find_packages(),
    version="0.1a10",
    license='GPLv3 License',
    author='Tarek Galal',
    ext_modules = [module_ext4],
    author_email='tare2.galal@gmail.com',
    description='Some android tools',
    platforms='any',
    classifiers =[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
