#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pwd
import grp
import sys

debug = True

# user name of the user who run decanter
user = pwd.getpwuid(os.getuid()).pw_name

# group name of the user who run decanter
group = grp.getgrgid(os.getegid()).gr_name

# if you run '/path/to/decanter.py', it becomes like '/path/to'
decanterpath = os.path.dirname(os.path.realpath(sys.argv[0]))

# file generated by decanter will be placed here
genpath = os.path.join(decanterpath, 'gen')

# pid file
pidfile = os.path.join(genpath, 'run', 'decanter_{0}.py')

# logging
logger = {
    # log directory path, first {0} is the port number and second {1] is the date
    'filepath': os.path.join(genpath, 'log', 'decanter_{0}-{1}.log'),
    # DEBUG, INFO, WARNING, ERROR, FATAL
    'level': 'DEBUG'
}

# the application directory
apppath = os.path.join(decanterpath, 'app')

# default routes
default = {
    'bundle': 'home',
    'controller': 'index'
}

# list of plugins names to install by default
plugins = ['jinja2']
