from django.test import TestCase
from .models import Concert

# Create your tests here.
class TestViews(TestCase):
  
  def setUp(self):
        # Setup code to create a Concert instance for testing
        self.concert_data = {
            'city': 'city_test',
            'date': '2024-07-05',
            'price': '500',
        }

  
  def test_all_concerts(self):
    response = self.client.get('/concerts/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response,'concerts/concerts.html')
  
  def test_concert_detail(self):
    concert = Concert.objects.create(
                            city= self.concert_data['city'],
                            date= self.concert_data['date'],
                            price= self.concert_data['price'] )
    response = self.client.get(f'/concerts/{concert.id}/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response,'concerts/concert_detail.html')
  
  # def test_all_cocnerts(self):
  #   response = self.client.get('/concerts/')
  #   self.assertTemplateUsed(response,'concerts/concerts.html')
  
  # def test_all_cocnerts(self):
  #   response = self.client.get('/concerts/')
  #   self.assertTemplateUsed(response,'concerts/concerts.html')
  
  def test_delete_concert(self):
    concert = Concert.objects.create(
                            city= self.concert_data['city'],
                            date= self.concert_data['date'],
                            price= self.concert_data['price'] )
        # self.client.login(username='admin', password='adminpassword')
    response = self.client.get(f'/concerts/delete/{concert.id}/')
    self.assertEqual(response.status_code, 200)  # Redirect after successful deletion
    self.assertFalse(Concert.objects.filter(id=concert.id).exists())  # Check that concert is deleted