# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from pdfgen import __version__
from setuptools import setup, find_packages


with open("README.md") as readme_file:
    readme = readme_file.read()

with open("CHANGELOG.md") as changelog_file:
    changelog = changelog_file.read()


install_requirements = [
    "click==6.7",
    "Jinja2>=2.8,<3",
    "pdfkit==0.6.1",
]


setup(
    name='pdfgen',
    version=__version__,
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir={
        "pdfgen": "pdfgen"
    },
    py_modules=["pdfgen"],
    entry_points={"console_scripts": ['pdfgen = pdfgen.cli:cli']},
    description='A library that creates PDFs from Jinja templates.',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Niall Grant',
    license='Apache2',
    author_email='ngfgrant@gmail.com',
    url='https://github.com/ngfgrant/pdfgen',
    keywords=['pdf', 'templates', 'jinja', 'cli'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    python_requires='>=3',
    install_requires=install_requirements,
)
