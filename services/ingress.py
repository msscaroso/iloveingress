from services.nginx import BaseConfig


def translate_rules_to_locations(rules):
    locations = []
    for rule in rules:
        server_name = rule.get("host", "")
        for path in rule["http"]["paths"]:
            service_name = path['backend']['service_name']
            port = path['backend']['service_port']
            to = f"http://{service_name}:{port}"
            locations.append(
                {
                    "server_name": server_name,
                    "path": path["path"],
                    "to": to
                }
            )
    return locations


def translate_rules_to_nginx_conf(rules):
    nginx = BaseConfig()
    locations = translate_rules_to_locations(rules)
    for location in locations:
        nginx.add_location(
            **location
        )
    return nginx.as_str()
