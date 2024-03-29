from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class District(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    state = models.ForeignKey(State,on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(District,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name
