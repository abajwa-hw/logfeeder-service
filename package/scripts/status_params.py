#!/usr/bin/env python
from resource_management import *

# config object that holds the status related configurations declared in the -env.xml file
config = Script.get_config()

logfeeder_pid_dir = config['configurations']['logfeeder-env']['logfeeder_pid_dir']
logfeeder_pid_file = format("{logfeeder_pid_dir}/logfeeder.pid")
