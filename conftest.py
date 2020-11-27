# conftest.py

import pytest


def pytest_collection_modifyitems(config, items):
    keywordexpr = config.option.keyword
    markexpr = config.option.markexpr
    if keywordexpr or markexpr:
        return  # let pytest handle this

    skip_mymarker = pytest.mark.skip(reason='e2e not selected')
    for item in items:
        if 'e2e' in item.keywords:
            item.add_marker(skip_mymarker)

 # example from https://stackoverflow.com/questions/56374588/how-can-i-ensure-tests-with-a-marker-are-only-run-if-explicitly-asked-in-pytest?rq=1
