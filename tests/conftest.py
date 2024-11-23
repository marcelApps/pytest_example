import pytest
from time import sleep

@pytest.fixture(scope="module")
def common_suite_setup_and_teardown():
    print("SUITE SETUP")
    yield None
    print("SUITE TEARDOWN")

@pytest.fixture(scope="function")
def common_test_setup_and_teardown():
    print("test setup")
    sleep(2)
    yield None
    print("test teardown")
