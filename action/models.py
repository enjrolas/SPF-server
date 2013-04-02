from django.db import models

class Action(models.Model):
    actionType=models.TextField()
    actionCode=models.TextField()

