from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=150)
    birthdate = models.DateField()
    roles = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(max_length=100, choices=roles)

    def __str__(self):
        return self.name


