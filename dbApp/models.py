from django.db import models

# Create your models here.

class Text(models.Model):
    user_name = models.CharField(max_length=250)
    input_text = models.CharField(max_length=250)

    def __str__(self):
        return self.user_name