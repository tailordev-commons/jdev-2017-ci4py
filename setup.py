#!/usr/bin/env python
from setuptools import setup


with open('README.md') as f:
    readme = f.read()


def parse_requirements(requirements, ignore=('setuptools',)):
    """Read dependencies from requirements file (with version numbers if any)

    Note: this implementation does not support requirements files with extra
    requirements
    """
    with open(requirements) as f:
        packages = set()
        for line in f:
            line = line.strip()
            if line.startswith(('#', '-r', '--')):
                continue
            if '#egg=' in line:
                line = line.split('#egg=')[1]
            pkg = line.strip()
            if pkg not in ignore:
                packages.add(pkg)
        return packages


setup(
    name='climate',
    version=__import__('climate').__version__,
    author='TailorDev',
    author_email='commons@tailordev.fr',
    packages=['climate', ],
    include_package_data=True,
    url='https://github.com/tailordev-commons/jdev-2017-ci4py',
    license='CC BY-SA 4.0',
    description=' '.join(__import__('climate').__doc__.splitlines()).strip(),  # noqa
    long_description=readme,
    classifiers=[
        'Topic :: Scientific/Engineering :: Visualization',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
    ],
    install_requires=parse_requirements('requirements.txt'),
    tests_require=parse_requirements('requirements-dev.txt'),
    scripts=['bin/factrump', ],
    package_data={'climate': ['data/*.csv']},
    keywords='python pytest climate',
)
