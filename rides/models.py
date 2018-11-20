from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.username


class Ride(models.Model):
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    date = models.DateField()
    passengers = models.IntegerField()
    driver = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='rides')

    def __str__(self):
        return self.origin
