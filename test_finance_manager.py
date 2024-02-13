import unittest
import pandas as pd
from finance_manager import FinanceManager, create_transaction
from transaction import Transaction
from datetime import datetime


class TestFinanceManager(unittest.TestCase):
    finance_manager = None
    
    @classmethod
    def setUpClass(cls):
        # Set up a FinanceManager instance with a test CSV file
        cls.finance_manager = FinanceManager('test_transactions.csv')
        
        # Preparing a test transactions CSV file with headers
        cls.finance_manager.transactions.to_csv(
            'test_transactions.csv', index = False
            )
    
    def test_load_transactions(self):
        # Test loading transactions from a CSV file
        self.finance_manager.load_transactions()
        self.assertIsInstance(self.finance_manager.transactions, pd.DataFrame)
    
    def test_add_transaction(self):
        # Test adding a new transaction
        test_transaction = create_transaction(
            '01/01/24', 20.0, 'Test',
            'Unit test transaction'
            )
        self.finance_manager.add_transaction(test_transaction)
        self.assertIn(
            'Test',
            self.finance_manager.transactions['Category'].values
            )
    
    def test_calculate_totals_by_category(self):
        # Test calculating totals by category
        totals = self.finance_manager.calculate_totals_by_category()
        self.assertIn('Test', totals.index)
    
    def test_date_validation(self):
        # Test that date validation works for transactions
        future_date = (datetime.now() + pd.DateOffset(days = 1)).strftime(
            '%m/%d/%y'
            )
        with self.assertRaises(ValueError):
            Transaction(future_date, 10, 'Test',
                        'Future date transaction')


if __name__ == '__main__':
    unittest.main()
