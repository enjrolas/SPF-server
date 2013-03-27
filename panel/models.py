from django.db import models

# Create your models here.
class Panel(models.Model):
    panelId = models.TextField()
    length=models.FloatField()
    margin=models.FloatField()
    active_area=models.FloatField()
    active_margin=models.FloatField()
    stroke_lead=models.FloatField()
    stroke_end=models.FloatField()
    full_stroke=models.FloatField()
    voltage=models.FloatField()
    solette_spacing=models.FloatField()
    solette_length=models.FloatField()
    initial_stroke=models.FloatField()
