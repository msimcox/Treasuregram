from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# If the user is deleted, the object will update the user to "deleted". Alternative is cascade delete, which would delete the object when the user is deleted.
def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Treasure(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user),)
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='treasure_images', default='media/default.png')

    def __str__(self):
        return self.name