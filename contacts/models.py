from django.db import models
from django.core.validators import EmailValidator

class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(validators=[EmailValidator()])
    
    def __str__(self):
        return self.name