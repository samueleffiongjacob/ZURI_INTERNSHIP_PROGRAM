from django.db import models

# Create your models here.


class Schools(models.Model):
    name = models.CharField(max_length=23)
    address = models.CharField(max_length=23)
    number_of_persons = models.CharField(max_length=23)
    email_of_school = models.EmailField

    def __str__(Self) -> str:
        return Self.name


class Country(models.Model):
    name = models.CharField(max_length=23)
    geo_location = models.CharField(max_length=23)
    number_of_persons = models.CharField(max_length=23)

    def __str__(Self) -> str:
        return Self.name


class State(models.Model):
    name = models.CharField(max_length=23)
    geo_location = models.CharField(max_length=23)
    number_of_persons = models.CharField(max_length=23)

    def __str__(Self) -> str:
        return Self.name


class Local_Government(models.Model):
    name = models.CharField(max_length=23)
    geo_location = models.CharField(max_length=23)
    number_of_persons = models.CharField(max_length=23)

    def __str__(Self) -> str:
        return Self.name


class village(models.Model):
    name = models.CharField(max_length=23)
    geo_location = models.CharField(max_length=23)
    number_of_persons = models.CharField(max_length=23)

    def __str__(Self) -> str:
        return Self.name
