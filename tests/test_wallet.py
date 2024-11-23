"""Test wallet app."""

import pytest


from core.wallet import InsufficientAmount


def test_default_initial_amount(empty_wallet):
    """test_default_initial_amount"""
    assert empty_wallet.balance == 0


def test_setting_initial_amount(wallet):
    """test_setting_initial_amount"""
    assert wallet.balance == 20


def test_wallet_add_cash(wallet):
    """test_wallet_add_cash"""
    wallet.add_cash(80)
    assert wallet.balance == 100


def test_wallet_spend_cash(wallet):
    """test_wallet_spend_cash"""
    wallet.spend_cash(10)
    assert wallet.balance == 10


@pytest.mark.error
def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    """test_wallet_spend_cash_raises_exception_on_insufficient_amount"""
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)


@pytest.mark.parametrize(
    "earned,spent,expected",
    [
        (30, 10, 20),
        (20, 2, 18),
    ],
)
def test_transactions(empty_wallet, earned, spent, expected):
    """test_transactions"""
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    assert empty_wallet.balance == expected
