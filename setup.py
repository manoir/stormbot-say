#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='stormbot',
      version='1.2',
      description='XMPP bot',
      author='Paul Fariello',
      author_email='paul@fariello.eu',
      url='https://git.paulfariello.fr/Stormbot',
      packages=find_packages(),
      package_data={'stormbot': ['data/*.dic']},
      scripts=['scripts/stormbot'],
      install_requires=['sleekxmpp', 'dnspython', 'gtts'],
      classifiers=['Environment :: Console',
                   'Intended Audience :: System Administrators',
                   'Operating System :: POSIX',
                   'Programming Language :: Python'])
