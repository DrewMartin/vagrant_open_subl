#! /usr/bin/env python

VAGRANT_SOURCE_PREFIX = "/home/vagrant/src"
HOST_SOURCE_DIR = "/Users/drewmartin/code/src"
EDITOR_BIN = "/opt/boxen/bin/subl"

import sys
import re
from subprocess import call

if len(sys.argv) < 2:
  sys.exit(-1)

path = ""

m = re.search('(\S+)$', sys.argv[1])
if m:
  path += m.group(1)

if len(sys.argv) > 2:
  m = re.search('^(\S+)(?: @ line (\d+))?', sys.argv[2])
  if m:
    path += m.group(1)

    if len(m.groups()) > 2 and m.group(2):
      path += ":" + m.group(2)

if path.startswith(VAGRANT_SOURCE_PREFIX):
  path = path.replace(VAGRANT_SOURCE_PREFIX, HOST_SOURCE_DIR, 1)

f = open('/Users/drewmartin/vagrant_open_log.txt', 'a')
f.write(path + "\n")

call([EDITOR_BIN, path])

# /Users/drewmartin/vagrant_open_subl.py \3 \4
