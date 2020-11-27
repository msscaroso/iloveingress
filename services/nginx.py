from collections import defaultdict

from nginx.config.api import Location
from configbuilder.main import ModifiedSection, ModifiedConfig

class BaseConfig(object):
    def __init__(self):
        self._servers = defaultdict(list)

    def as_str(self):
        return str(self._build_config())

    def add_location(self, server_name, path, to):
        self._servers[server_name].append(Location(
            location=path,
            proxy_pass=to
        ))
        return

    def _build_config(self):
        events = ModifiedSection("events")
        http = ModifiedSection("http")
        if not self._servers:
            http.sections.add(
                ModifiedSection(
                    "server",
                )
            )
        items = []
        for server, locations in self._servers.items():
            kwargs = {}
            if server:
                kwargs["server_name"] = server
            items.append(
                ModifiedSection(
                    "server",
                    *locations,
                    **kwargs
                )
            )
        http.sections.add(*items)
        return ModifiedConfig(
            events,
            http
        )
