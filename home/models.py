from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=122)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Detail(models.Model):
    collegename = models.CharField(max_length=120)
    collegrank = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.collegename


class College_Info(models.Model):
    collegename = models.CharField(max_length=120)
    collegrank = models.CharField(max_length=100)
    colleadd = models.CharField(max_length=100)
    TotalBranch = models.IntegerField()
    Hostel = models.CharField(max_length=20)
    collegeReviews = models.TextField()

    def __str__(self):
        return self.collegename
