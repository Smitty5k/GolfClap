from django.db import models

# Create your models here.
class TeePositionColor(models.Model):
    color = models.CharField(max_length=50)
    def __unicode__(self):
        return self.color

class TeePosition(models.Model):
    color = models.ForeignKey(TeePositionColor)
    distance = models.IntegerField()
    def __unicode__(self):
        return self.color.color+"-"+str(self.distance)

class Hole(models.Model):
    number = models.IntegerField()
    par = models.IntegerField()
    #image = models.ImageField(upload_to=)
    handicap = models.IntegerField()
    teePositions = models.ManyToManyField(TeePosition)
    def __unicode__(self):
        return str(self.number)

class Course(models.Model):
    name = models.CharField(max_length=200)
    par = models.IntegerField()
    holeset = models.ManyToManyField(Hole)
    def __unicode__(self):
        return self.name

class GolfCourse(models.Model):
    name = models.CharField(max_length=200)
    courses = models.ManyToManyField(Course)
    #image = models.ImageField(upload_to=)
    def __unicode__(self):
        return self.name