#!/usr/bin/env python
import sys
import json

with open("local_settings.json") as f:
    config = json.load(f)

print config[sys.argv[1]]
