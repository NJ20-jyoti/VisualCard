from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission



class CustomUser(AbstractUser):
    nominee_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=20)
    dob = models.DateField()
    age = models.IntegerField()
    photo = models.ImageField(upload_to='profile_photos')
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    random_id = models.CharField(max_length=10, unique=True)