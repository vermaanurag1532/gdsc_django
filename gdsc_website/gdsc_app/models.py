from django.db import models

# Create your models here.


class Club_Coordinators(models.Model):
    full_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='uploads/club_coordinators')

    def __str__(self):
        return self.full_name


class CoreTeam(models.Model):
    full_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='uploads/coreTeam')

    def __str__(self):
        return self.full_name


class Our_Activities(models.Model):
    activity_name = models.CharField(max_length=256)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.activity_name


class Events(models.Model):
    title = models.CharField(max_length=256)
    info = models.CharField(max_length=256)
    date = models.DateField()

    def __str__(self):
        return self.title
