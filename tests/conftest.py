"""Configuration of tests module."""

from time import sleep

import pytest

from core.wallet import Wallet


@pytest.fixture(scope="module")
def common_suite_setup_and_teardown():
    """common_suite_setup_and_teardown"""
    print("SUITE SETUP")
    yield None
    print("SUITE TEARDOWN")


@pytest.fixture(scope="function")
def common_test_setup_and_teardown():
    """common_test_setup_and_teardown"""
    print("test setup")
    sleep(2)
    yield None
    print("test teardown")


@pytest.fixture
def empty_wallet(
    common_suite_setup_and_teardown, common_test_setup_and_teardown
):  # pylint: disable=unused-argument, redefined-outer-name
    """Returns a Wallet instance with a zero balance"""
    return Wallet()


@pytest.fixture
def wallet(
    common_suite_setup_and_teardown, common_test_setup_and_teardown
):  # pylint: disable=unused-argument, redefined-outer-name
    """Returns a Wallet instance with a balance of 20"""
    return Wallet(20)
