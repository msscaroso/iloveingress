import pytest

from services.apiserver import list_ingresses


@pytest.mark.e2e
class TestListIngresses(object):
    def test_list_all_ingresses(self):
        assert len(list_ingresses().items) == 1
