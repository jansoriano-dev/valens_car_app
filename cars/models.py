from django.db import models

# Create your models here.
class Car(models.Model):
    COLOR = (('Blue','Blue'),('Red','Red'),)
    name = models.CharField(max_length=200, null=True)
    color = models.CharField(max_length=200, null=True,choices=COLOR)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name