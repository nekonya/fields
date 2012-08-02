from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='fields',
      version=version,
      description="factory function for creating class instance as a named mutable container",
      long_description="""\
not described.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='container product-type',
      author='Tomohiro Miyasaka',
      author_email='neko@nekonya.com',
      url='http://www.nekonya.com/',
      license='New BSD License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
