from django.db import models

# Create your models here.
class Backing(models.Model):

    def getFields(self):
        return [(field.name, field.value_to_string(self)) for field in Panel._meta.fields]

    length=models.FloatField()
    solettes=models.IntegerField()
