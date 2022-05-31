from django.db import models

class OnlineUser(models.Model):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=16)
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name