from jadi import component
from aj.plugins.core.api.sidebar import SidebarItemProvider
import aj

aj.config.load()
if 'tinydb' not in aj.config.data:
    aj.config.data['tinydb'] = "/ajenti-persistent"

@component(SidebarItemProvider)
class ItemProvider(SidebarItemProvider):
    def __init__(self, context):
        pass

    def provide(self):
        return [
            {
                'attach': 'category:general',
                'name': _('Settings'),
                'icon': 'cog',
                'url': '/view/settings',
                'children': [
                ]
            }
        ]
