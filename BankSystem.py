class BankAccount:
    def __init__(self, name: str, account_number: str, initial_balance: float = 0.0):
        self.name = name
        self.account_number = account_number
        self._balance = initial_balance

    def deposit(self, amount: float) -> float:
        self._balance += amount
        return self._balance

    def withdraw(self, amount: float) -> float:
        self._balance -= amount
        return self._balance

    def withdraw_with_fee(self, amount: float, fee: float) -> float:
        total = amount + fee
        self._balance -= total
        return self._balance

    def show_balance(self) -> float:
        return self._balance

def main():
    name = input("Enter your name: ")
    account_number = input("Enter your account number: ")

    account = BankAccount(name, account_number)

    print(f"Welcome, {account.name}! Your account number is {account.account_number}.")
    print(f"Your balance is: {account.show_balance()}")

    while True:
        print("\n--- BANK SYSTEM ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Withdraw (with fee)")
        print("4. Show balance")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            try:
                amount = float(input("Enter an amount to deposit: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            account.deposit(amount)
            print(f"Balance after deposit: {account.show_balance()}")

        elif choice == "2":
            if account.show_balance() == 0:
                print("No amount to be withdrawn: balance is 0.")
                continue
            try:
                amount = float(input("Enter an amount to withdraw: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            account.withdraw(amount)
            print(f"Balance after withdrawal: {account.show_balance()}")

        elif choice == "3":
            if account.show_balance() == 0:
                print("No amount to be withdrawn: balance is 0.")
                continue
            try:
                amount = float(input("Enter an amount to withdraw: "))
                fee = 18
            except ValueError:
                print("Invalid amount. Please enter numbers.")
                continue

            account.withdraw_with_fee(amount, fee)
            print(f"Balance after withdrawal with fee: {account.show_balance()}")

        elif choice == "4":
            print(f"Current balance: {account.show_balance()}")

        elif choice == "5":
            print("End Program")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
