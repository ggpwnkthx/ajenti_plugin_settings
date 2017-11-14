# pyflakes: disable-all
from .main import *
from .views import *

import aj

def init(plugin_manager):
    aj.config.load()
    if 'tinydb' not in aj.config.data:
        aj.config.data['tinydb'] = "/ajenti-persistent"
    if aj.config.data['tinydb'] is "":
        aj.config.data['tinydb'] = "/ajenti-persistent"
    aj.config.save()