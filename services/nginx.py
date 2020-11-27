from nginx.config.api import Config, Section, Location


class BaseConfig(object):
    def __init__(self):
        self._locations = []

    def as_str(self):
        return str(self._build_config())

    def add_location(self, path, to):
        self._locations.append(Location(
            location=path,
            proxy_pass=to
        ))
        return

    def _build_config(self):
        events = Section("events")
        http = Section("http")
        http.sections.add(
            Section(
                "server",
                *self._locations
            )
        )
        return Config(
            events,
            http
        )
