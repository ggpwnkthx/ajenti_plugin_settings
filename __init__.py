# pyflakes: disable-all
from .main import *
from .views import *

import aj

def init(plugin_manager):
    aj.config.load()