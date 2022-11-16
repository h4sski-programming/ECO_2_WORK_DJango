from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CHOICES = ['bike', 'foot', 'scooter']


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    distance = models.IntegerField()
    vehicle = models.CharField(max_length=100, default='')
    date = models.DateField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.date} {self.user.username} {self.distance}'

    def get_vehicles(self):
        list = CHOICES
        return list
