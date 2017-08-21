#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='stormbot-say',
      version='1.2',
      description='text to speech plugin for stormbot',
      author='Paul Fariello',
      author_email='paul@fariello.eu',
      url='https://git.paulfariello.fr/Stormbot/stormbot-say',
      packages=find_packages(),
      install_requires=['stormbot', 'gtts'],
      entry_points={'stormbot.plugins': ['say = stormbot_say:Say']},
      classifiers=['Environment :: Console',
                   'Intended Audience :: System Administrators',
                   'Operating System :: POSIX',
                   'Programming Language :: Python'])
