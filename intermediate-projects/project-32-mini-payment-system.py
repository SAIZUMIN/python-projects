class Payment:
    def __init__(self, amount: int):
        self.amount = amount

    def pay(self):
        return 'Hi, Please settle your payment amount. Thank you!'

class CashPayment(Payment):
    def pay(self):
        print('=== CASH PAYMENT ===')
        print('Cash payment successful!')
        print(f'Amount: {self.amount}')
        print('====================')


class CardPayment(Payment):
    def pay(self):
        print('=== CARD PAYMENT ===')
        print('Card payment successful!')
        print(f'Amount: {self.amount}')
        print('====================')

class EWalletPayment(Payment):
    def pay(self):
        print('=== E-WALLET PAYMENT ===')
        print('E-wallet payment successful!')
        print(f'Amount: {self.amount}')
        print('========================')

class BankTransferPayment(Payment):
    def pay(self):
        print('=== Bank Transfer PAYMENT ===')
        print('Bank Transfer payment successful!')
        print(f'Amount: {self.amount}')
        print('========================')



payment = CashPayment(500)
payment2 = CardPayment(500)
payment3 = EWalletPayment(500)
payment4 = BankTransferPayment(1000)

payment.pay()
payment2.pay()
payment3.pay()
payment4.pay()




