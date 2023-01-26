from unittest import TestCase
from app import app
from forex_python.converter import CurrencyRates, CurrencyCodes

c = CurrencyRates(force_decimal=False)
cc = CurrencyCodes()

app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class FlaskTests(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_homepage(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<input type="text" name="inputcurrency"', html)

    def test_dollar_conversion(self):
            self.assertEqual(c.convert("USD", "USD", 1), 1)
            self.assertEqual(c.convert("GBP", "GBP", 1), 1)
            self.assertEqual(c.convert("JPY", "JPY", 1), 1)
            