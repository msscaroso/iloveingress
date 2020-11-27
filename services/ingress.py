from services.nginx import BaseConfig


def translate_rules_to_nginx_conf(rules):
    nginx = BaseConfig()
    for rule in rules:
        server_name = rule.get("host", "")
        for path in rule["http"]["paths"]:
            service_name = path['backend']['service_name']
            port = path['backend']['service_port']
            to = f"http://{service_name}:{port}"
            nginx.add_location(
                server_name=server_name,
                path=path["path"],
                to=to
            )

    return nginx.as_str()
