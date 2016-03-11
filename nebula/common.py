import os
import sys
import socket
import json

from nxtools import *

class Config(dict):
    def __init__(self):
        super(Config, self).__init__()
        self["site_name"] = "Unnamed"
        self["user"] = "Setup"              # Service identifier. Should be overwritten by service/script.
        self["host"] = socket.gethostname()  # Machine hostname
        if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
            local_settings_path = sys.argv[1]
        else:
            local_settings_path = "local_settings.json"
        try:
            local_settings = json.loads(open(local_settings_path).read())
        except:
            print (local_settings_path)
            log_traceback(handlers=False)
            critical_error("Unable to open site_settings file.")
        self.update(local_settings)

config = Config()
logging.user = config["user"]
