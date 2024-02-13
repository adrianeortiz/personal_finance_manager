from datetime import datetime


class Transaction:
    def __init__(self, date, amount, category, description):
        if not self._validate_date(date):
            raise ValueError(
                'Transaction date is in the future. '
                'Please enter a valid date.'
                )
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description
    
    def to_dict(self):
        return {
            'Date': self.date,
            'Amount': self.amount,
            'Category': self.category,
            'Description': self.description
            }
    
    def _validate_date(self, date_str):
        transaction_date = datetime.strptime(date_str, '%m/%d/%y')
        return transaction_date <= datetime.now()
