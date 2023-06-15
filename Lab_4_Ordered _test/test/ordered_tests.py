import unittest
from finance import Budget, CurrencyConverter

class BudgetTest(unittest.TestCase):
    def setUp(self):
        self.budget = Budget(100, 'USD')

    def test_initial_balance(self):
        self.assertEqual(self.budget.get_balance(), 100)

    def test_update_balance(self):
        self.budget.update_balance(50)
        self.assertEqual(self.budget.get_balance(), 150)

    def test_negative_update_balance(self):
        self.budget.update_balance(-50)
        self.assertEqual(self.budget.get_balance(), 50)

    def test_get_balance_with_currency(self):
        balance_with_currency = self.budget.get_balance_with_currency()
        self.assertEqual(balance_with_currency, "Поточний баланс: 100 USD")

class CurrencyConverterTest(unittest.TestCase):
    def setUp(self):
        exchange_rates = {'USD': 1.0, 'EUR': 0.85, 'GBP': 0.72}
        self.converter = CurrencyConverter(exchange_rates)

    def test_convert_same_currency(self):
        converted_amount = self.converter.convert(100, 'USD', 'USD')
        self.assertEqual(converted_amount, 100)

    def test_convert_valid_currencies(self):
        converted_amount = self.converter.convert(100, 'USD', 'EUR')
        self.assertEqual(converted_amount, 85)

    def test_convert_invalid_currencies(self):
        converted_amount = self.converter.convert(100, 'USD', 'JPY')
        self.assertEqual(converted_amount, "Invalid currencies")

if __name__ == '__main__':
    unittest.main()