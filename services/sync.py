import subprocess
from services.apiserver import list_ingresses
from services.ingress import translate_locations_to_nginx_conf, translate_rules_to_locations


def sync_ingress():
    ingresses = list_ingresses()
    locations = []
    for ingress in ingresses.items:
        ing = ingress.to_dict()
        locations += translate_rules_to_locations(ing['spec']['rules'])
    conf = translate_locations_to_nginx_conf(locations)
    with open("conf/nginx.conf", mode="w+") as conf_file:
        conf_file.write(conf)
    subprocess.run(["nginx", "-s", "reload"])
