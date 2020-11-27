from services.nginx import BaseConfig
from tests.common import load_file_from_resources


class TestGenerateConfigFile(object):

    def test_initial_config_is_sample_config(self):
        expected_conf = load_file_from_resources("nginx/expected.conf")
        nginx_conf = BaseConfig()
        assert nginx_conf.as_str() == expected_conf

    def test_add_location(self):
        expected_conf = load_file_from_resources("nginx/location.conf")
        nginx_conf = BaseConfig()
        nginx_conf.add_location(
            server_name="",
            path="/",
            to="http://example.com"
        )
        assert nginx_conf.as_str() == expected_conf

    def test_add_multiple_locations(self):
        expected_conf = load_file_from_resources("nginx/multiple_locations.conf")
        nginx_conf = BaseConfig()
        nginx_conf.add_location(
            server_name="",
            path="/",
            to="http://example.com"
        )
        nginx_conf.add_location(
            server_name="",
            path="/test",
            to="http://another.com"
        )
        assert nginx_conf.as_str() == expected_conf
