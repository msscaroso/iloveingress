from kubernetes import config, client


def list_ingresses():
    config.load_kube_config()
    v1 = client.ExtensionsV1beta1Api()
    return v1.list_ingress_for_all_namespaces()

