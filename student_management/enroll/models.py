from django.db import models

# Model to store user data
class User(models.Model):
    # Name of the user
    name = models.CharField(max_length=70)
    
    # Email field for storing the user's email
    email = models.EmailField(max_length=100)
    
    # Password field for storing the user's password
    password = models.CharField(max_length=100)
