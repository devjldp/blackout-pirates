from django.test import TestCase
from .forms import ConcertForm


class ConcertFormTest(TestCase):

    def setUp(self):
        # Setup code to create a Concert instance for testing
        self.concert_data = {
            'city': 'city_test',
            'date': '2024-07-05',
            'price': '500',
        }

    def test_form_fields_placeholder(self):
        form = ConcertForm()
        self.assertEqual(form.fields['city'].widget.attrs['placeholder'], 'City')
        self.assertEqual(form.fields['date'].widget.attrs['placeholder'], 'Date')
        self.assertEqual(form.fields['price'].widget.attrs['placeholder'], 'Price £')


    def test_form_valid_data(self):
        form = ConcertForm(data=self.concert_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        invalid_data = {
            'city': '',  # Empty city
            'date': 'invalid-date',  # Invalid date format
            'price': 'not-a-number',  # Invalid price
        }
        form = ConcertForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('city', form.errors)
        self.assertIn('date', form.errors)
        self.assertIn('price', form.errors)