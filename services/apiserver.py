from kubernetes import config, client
from kubernetes.config import ConfigException


def list_ingresses():
    try:
        config.load_incluster_config()
    except ConfigException:
        config.load_kube_config()
    v1 = client.ExtensionsV1beta1Api()
    return v1.list_ingress_for_all_namespaces()

