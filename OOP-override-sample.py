
from abc import ABC, abstractmethod
from decimal import Decimal, InvalidOperation


class Payment(ABC):
    def __init__(self, amount: Decimal | int | float | str):
        try:
            self.amount = Decimal(str(amount))
        except (InvalidOperation, ValueError):
            raise ValueError("Invalid payment amount.")

        if not self.amount.is_finite() or self.amount <= 0:
            raise ValueError("Payment amount must be positive and finite.")

    @abstractmethod
    def pay(self) -> None:
        """Process this payment method."""
        pass

    def _show_success(self, method: str) -> None:
        print(f"=== {method.upper()} PAYMENT ===")
        print(f"{method} payment successful!")
        print(f"Amount: {self.amount:.2f}")
        print("=" * (len(method) + 18))


class CashPayment(Payment):
    def pay(self) -> None:
        self._show_success("Cash")


class CardPayment(Payment):
    def pay(self) -> None:
        self._show_success("Card")


class EWalletPayment(Payment):
    def pay(self) -> None:
        self._show_success("E-Wallet")


class BankTransferPayment(Payment):
    def pay(self) -> None:
        self._show_success("Bank Transfer")


def main() -> None:
    payments: list[Payment] = [
        CashPayment(500),
        CardPayment(500),
        EWalletPayment(500),
        BankTransferPayment(1000),
    ]

    for payment in payments:
        payment.pay()
        print()


if __name__ == "__main__":
    main()