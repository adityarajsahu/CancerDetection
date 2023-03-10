from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class breastImage(models.Model):
    xrayImage = models.ImageField(upload_to='xrayImages/')
    uploadedBy = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    uploadedOn = models.DateTimeField(auto_now_add=True)
    maskImage = models.ImageField(upload_to='segmentedImages/')