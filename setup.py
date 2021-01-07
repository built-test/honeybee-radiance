#!/usr/bin/env python
import setuptools
# add these line to integrate the queenbee packaging process
# into Python packaging
from queenbee_dsl.package import PackageQBInstall, PackageQBDevelop
name = 'pollination-honeybee-radiance'
PackageQBInstall.__queenbee_name__ = name
PackageQBDevelop.__queenbee_name__ = name

# normal setuptool inputs
setuptools.setup(
    cmdclass={
        'develop': PackageQBDevelop,
        'install': PackageQBInstall
    },
    name=name,
    author='mostapha',
    author_email='mostapha@ladybug.tools',
    setup_requires=['setuptools_scm'],
    packages=setuptools.find_packages('pollination_honeybee_radiance'),
    keywords=['honeybee', 'radiance', 'ladybug-tools', 'daylight'],
    license='PolyForm Shield License 1.0.0'
)