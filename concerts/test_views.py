from django.test import TestCase
from .models import Concert
from django.urls import reverse
from django.contrib.auth.models import User


# Create your tests here.
class TestViews(TestCase):
  
  def setUp(self):
        # Setup code to create a Concert instance for testing
        self.concert_data = {
            'city': 'city_test',
            'date': '2024-07-05',
            'price': '500',
        }
        # Create a regular user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Create a superuser
        self.superuser = User.objects.create_superuser(username='adminuser', password='adminpassword')
  
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
  
  def test_add_concert_user(self):
    self.client.login(username='testuser', password='testpassword')
    response = self.client.get('/concerts/add/')
    self.assertRedirects(response, reverse('home'))
    
  def test_superuser_access(self):
    # Log in as the superuser
    self.client.login(username='adminuser', password='adminpassword')
          
    # Make a request to the add concert view
    response = self.client.get(reverse('add_concert'))
          
    # Check that the user was not redirected
    self.assertEqual(response.status_code, 200)  