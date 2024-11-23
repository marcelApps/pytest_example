"""Wallet app."""

class InsufficientAmount(Exception):
    """InsufficientAmount wallet error."""

class Wallet:
    """Main app class."""

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount: float):
        """Spend cash in the wallet if available."""
        if self.balance < amount:
            raise InsufficientAmount(f'Not enough available to spend {amount}')
        self.balance -= amount

    def add_cash(self, amount: float):
        """Add cash to the wallet."""
        self.balance += amount
