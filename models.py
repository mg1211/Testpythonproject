from django.db import models

# Create your models here.
class Examqp(models.Model):
    Question = models.CharField(max_length=100)
    Option1 = models.CharField(max_length=100)
    Option2 = models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100)
    Corrans = models.CharField(max_length=100)
class Meta:
    db_table = "test"
