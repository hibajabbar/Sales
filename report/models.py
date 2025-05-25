from django.db import models

class sale(models.Model):
    user=models.CharField(max_length=30)
    passwords=models.CharField(max_length=20)
    