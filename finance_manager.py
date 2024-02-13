import pandas as pd
from datetime import datetime
from transaction import Transaction


def validate_date(date_str):
    transaction_date = datetime.strptime(date_str, '%m/%d/%y')
    return transaction_date <= datetime.now()


class FinanceManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.transactions = self.load_transactions()
    
    def load_transactions(self):
        try:
            return pd.read_csv(self.file_path)
        except FileNotFoundError:
            return pd.DataFrame(
                columns = ['Date', 'Amount', 'Category', 'Description']
                )
    
    def add_transaction(self, transaction):
        if validate_date(transaction.date):
            self.transactions = self.transactions.append(
                transaction.to_dict(), ignore_index = True
                )
            self.save_transactions()
        else:
            raise ValueError(
                'Transaction date is in the future. '
                'Please enter a valid date.'
                )
    
    def save_transactions(self):
        self.transactions.to_csv(self.file_path, index = False)
    
    def list_transactions(self):
        return self.transactions
    
    def calculate_totals_by_category(self):
        return self.transactions.groupby('Category')['Amount'].sum()
    
    def get_transactions_in_date_range(self, start_date, end_date):
        mask = ((self.transactions['Date'] >= start_date) & (
                self.transactions['Date'] <= end_date))
        return self.transactions.loc[mask]


# Helper function to create a Transaction object from user input
def create_transaction(date, amount, category, description):
    return Transaction(date, amount, category, description)
