from django.db import models

# Create your models here.


class Dish(models.Model):
    
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, default="", null=True, blank=True)
    items = models.JSONField(default=dict, null=True, blank=True)
    lat_long = models.CharField(max_length=255, default="", null=True, blank=True)
    full_details = models.JSONField(default=dict, null=True, blank=True)

    def __str__(self):
        return self.name

