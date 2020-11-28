import pytest

from services.ingress import translate_locations_to_nginx_conf, translate_rules_to_locations
from tests.common import load_file_from_resources


class TestIngressService(object):

    @pytest.fixture
    def rules(self):
        return [{'host': None,
                 'http': {'paths': [{'backend': {'service_name': 'nginx', 'service_port': 80},
                                     'path': '/testpath'}]}},
                {'host': 'web',
                 'http': {'paths': [{'backend': {'service_name': 'web', 'service_port': 8080},
                                     'path': '/'}]}},
                {'host': 'web2',
                 'http': {'paths': [{'backend': {'service_name': 'web', 'service_port': 8080},
                                     'path': '/test'}]}}]

    def test_create_nginx_conf_from_rules(self, rules):
        expected_conf = load_file_from_resources("nginx/from_ingress_rules.conf")
        locations = translate_rules_to_locations(rules)
        conf = translate_locations_to_nginx_conf(locations)
        assert conf == expected_conf
