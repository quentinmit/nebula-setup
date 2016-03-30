from .core import *
from .db import *
from .helpers import *


from .template_meta import meta_types
from .template_folders import folders

template_data = {
        "meta_types" : meta_types,
        "folders" : folders,
        "cs" : [],
        "settings" : [],
        "actions" : {},
        "channels" : {},
        "services" : {},
        "storages" : {},
        "views" : {}
        }
