from .folders import *
from .actions import *
from .meta_types import *
from .settings import *
from .views import *
from .channels import *
from .storages import *
from .services import *

__all__ = ["data"]

data = {
        "folders" : FOLDERS,
        "actions" : ACTIONS,
        "meta_types" : META_TYPES,
        "settings" : SETTINGS,
        "views" : VIEWS,
        "channels" : CHANNELS,
        "storages" : STORAGES,
        "services" : SERVICES
    }
