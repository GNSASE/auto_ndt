#!/usr/bin/env python
"""
This configuration file is used to provide the run.py harness information regarding this
code base information.
"""
from distutils.core import setup
import ConfigParser
import os
import sys

#######
# Append lib directory to path
working_dir =  '{}/lib'.format(os.getcwd())
sys.path.append(working_dir)

#######
# Gather files from within the bin | lib | test directories and sub-directories
def walk_directory(directory_name, filelist=[]):
    for root, subFolders, files in os.walk(directory_name):
        for file in files:
            if '.pyc' not in file:
                filelist.append(os.path.join(root,file))
    return filelist

bin = walk_directory('bin')
lib = walk_directory('lib')
test = walk_directory('test')


########
# Read configuration file
config = ConfigParser.RawConfigParser()
config.read('configuration/default.cfg')

setup(name=config.get('Section1', 'app_name'),
      version=config.get('Section1', 'version'),
      description=config.get('Section1', 'description'),
      author=config.get('Section1', 'author'),
      author_email='{}@microsoft.com'.format(config.get('Section1', 'alias')),
      url=config.get('Section1', 'external_doc_url'),
      packages=['distutils', 'distutils.command',
                'example_library',
                'rainbow_logging_handler',
                'nose',
                'sphinx'],
      data_files=bin,
      package_dir = {'': 'lib'},
     )

