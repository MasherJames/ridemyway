from django.test import TestCase
from .models import Ride, User


class RideTest(TestCase):
    '''
    Ride model test
    '''
    def setUp(self):
        user = User.objects.create(username='james', email='jamesmasher13@gmail.com')
        Ride.objects.create(driver=user, origin='Nakuru', destination='Naivasha', passengers=7)
        Ride.objects.create(driver=user, origin='Juja', destination='githu', passengers=9)

    def test_models_can_create_ride(self):
        ''' test model can create a ride '''
        ride_naks = Ride.objects.get(origin='Nakuru')
        ride_juja = Ride.objects.get(origin='Juja')
        self.assertEquals(ride_naks.created_ride(), 'Ride from Nakuru to Naivasha created')
        self.assertEquals(ride_juja.created_ride(), 'Ride from Juja to githu created')