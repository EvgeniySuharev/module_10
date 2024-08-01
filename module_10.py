import threading


class BankAccount:
    lock = threading.Lock()

    def __init__(self, balance=1000):
        self.balance = balance

    def deposit(self, amount):
        self.lock.acquire()
        self.balance += amount
        self.lock.release()
        print(f'Deposited {amount}, new balance is {self.balance}')

    def withdraw(self, amount):
        self.lock.acquire()
        self.balance -= amount
        self.lock.release()
        print(f'Withdrew {amount}, new balance is {self.balance}')


def deposit_task(bank_account, amount):
    for _ in range(5):
        bank_account.deposit(amount)


def withdraw_task(bank_account, amount):
    for _ in range(5):
        bank_account.withdraw(amount)


account = BankAccount()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
