from finance_manager import FinanceManager
from transaction import Transaction

csv_file_path = 'transactions.csv'

finance_manager = FinanceManager(csv_file_path)


def get_transaction_from_user():
    date = input("Enter the date (MM/DD/YYYY): ")
    amount = float(input("Enter the amount: "))
    category = input("Enter the category: ")
    description = input("Enter a description: ")
    return Transaction(date, amount, category, description)


def add_transaction():
    try:
        transaction = get_transaction_from_user()
        finance_manager.add_transaction(transaction)
        print("Transaction added successfully.")
    except ValueError as v_error:
        print(v_error)


def list_transactions():
    transactions = finance_manager.list_transactions()
    print(transactions)


def show_totals_by_category():
    totals = finance_manager.calculate_totals_by_category()
    print(totals)


def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Add a new transaction")
        print("2. List all transactions")
        print("3. Show totals by category")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_transaction()
        elif choice == '2':
            list_transactions()
        elif choice == '3':
            show_totals_by_category()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
