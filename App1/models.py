from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.TextField(max_length=500, blank=True)
    country = models.TextField(max_length=500, blank=True)
    
   
    # Add more fields as needed

    # Add any additional methods or properties if required

    def __str__(self):
        return self.user.username

# # Create your models here.
# class Score(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     field1 = models.CharField(max_length=255)
#     field2 = models.CharField(max_length=255)
#     score = models.FloatField()

#     def __str__(self):
#         return f"Score: {self.score}"
