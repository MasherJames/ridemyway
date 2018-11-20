from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.username


class Ride(models.Model):
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    passengers = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    driver = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='rides')

    def created_ride(self):
        return 'Ride from ' + self.origin + ' to ' + self.destination + ' created'

    def __str__(self):
        return self.origin
