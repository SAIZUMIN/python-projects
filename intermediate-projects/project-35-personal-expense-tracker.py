import json

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, name: str, amount: int):            
        if type(name) is not str or not name.strip():
            raise ValueError ('Invalid name')
        if type(amount) is not int or amount <= 0:
            raise ValueError('Invalid amount')
        
        expense = {
            "name": name.strip(),
            "amount": amount
        }
        self.expenses.append(expense)

    def view_expenses(self):
        if not self.expenses:
            print('No expenses found')
        else:
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. {expense['name']} - ₱{expense['amount']}")

    def calculate_total(self):
        total = 0
        for amount in self.expenses:
            total += amount['amount']
        return total

    def save_expenses(self, filename="expenses.json"):
        try:
            with open(filename, "w") as file:
                json.dump(self.expenses, file, indent=4)
            print(f'Expenses successfully saved to {filename}')
        except OSError as e:
            print(f'Failed to save expenses: {e}')

    def load_expenses(self, filename="expenses.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
            
            if not isinstance(data, list):
                print(f'{filename} contains invalid data structure')
                return

            temp_expenses = []
            for item in data:
                if not isinstance(item, dict) or "name" not in item or "amount" not in item:
                    print(f'{filename} contains invalid expense records')
                    return
                if not isinstance(item["name"], str) or not item["name"].strip():
                    print(f'{filename} contains an invalid name')
                    return
                if type(item["amount"]) is not int or item["amount"] <= 0:
                    print(f'{filename} contains an invalid amount')
                    return
                
                temp_expenses.append({
                    "name": item["name"].strip(),
                    "amount": item["amount"]
                })

            self.expenses = temp_expenses
            print(f'Expenses successfully loaded from {filename}')

        except FileNotFoundError:
            print(f'No save file from {filename}')

        except json.JSONDecodeError:
            print(f'{filename} was corrupted or empty')

        except OSError as e:
            print(f'Failed to read expenses: {e}')

tracker = ExpenseTracker()
tracker.load_expenses()

while True:
    print('=== PERSONAL TRACKER ===')
    print('1. Add Expense')
    print('2. View Expenses')
    print('3. View Total Expenses')
    print('4. Exit')

    choice = input('Enter choice: ')
    if choice == '1':
        try:
            name = input('Enter name: ')
            amount = int(input('Enter amount: '))
            
            tracker.add_expense(name, amount)
            print(f'Expenses: {name} - ₱{amount} successfully added!')
            tracker.save_expenses()

        except ValueError as e:
            print(f'Invalid: {e}')

    elif choice == '2':
        tracker.view_expenses()

    elif choice == '3':
        print(f'Total expense: ₱{tracker.calculate_total()}')

    elif choice == '4':
        tracker.save_expenses()
        print('Thank you for using Expense Tracker')
        break

    else:
        print('Invalid choice')
        




        