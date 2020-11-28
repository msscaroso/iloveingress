from nginx.config.api import Config, Section
from nginx.config.api.options import AttrDict
"""
This fixes a small bug in nginx-config-builder lib.
The bug: It is not possible to add more than one 'server' directive.
"""


class AttrList(AttrDict):
    """ A dictionary/list hybrid that exposes values as attributes. """
    def __iter__(self):
        return iter(self.values())

    def append(self, item):
        if hasattr(item, '_parent'):
            item._parent = self._owner
        if hasattr(item, 'name') and item.name != "server":
            self[item.name] = item
        else:
            self[hash(item)] = item

    def add(self, *items):
        for item in items:
            self.append(item)



class ModifiedConfig(Config):

    def __init__(self, *sections, **options):
        """ Create an EmptyBlock. """
        self.sections = AttrList(self)
        self.options = AttrDict(self)

        self._set_directives(*sections, **options)


class ModifiedSection(Section):

    def __init__(self, name, *sections, **options):
        self.name = name
        self.sections = AttrList(self)
        self.options = AttrDict(self)

        self._set_directives(*sections, **options)
