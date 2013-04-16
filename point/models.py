from django.db import models

class Point(models.Model):
    pointType=models.TextField()
    code=models.TextField()
    position=models.FloatField()
    remainingDistance=models.FloatField()
    panelID=models.IntegerField()
    
    def __str__(self):
        return "%s position:  %s from backing, %s from target" % (self.pointType, self.position, self.remainingDistance)

    def __repr__(self):
        return "%s position:  %s from backing, %s from target" % (self.pointType, self.position, self.remainingDistance)
