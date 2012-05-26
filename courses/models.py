from django.db import models

# Create your models here.
class GolfCourse(models.Model):
    name = models.CharField(max_length=200)
    #image = models.ImageField(upload_to=)
    def __unicode__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    par = models.IntegerField()
    golf_course = models.ForeignKey(GolfCourse)
    def __unicode__(self):
        return str(self.golf_course)+"-"+self.name


class TeePositionColor(models.Model):
    color = models.CharField(max_length=50)
    def __unicode__(self):
        return self.color

class Hole(models.Model):
    number = models.IntegerField()
    par = models.IntegerField()
    #image = models.ImageField(upload_to=)
    handicap = models.IntegerField()
    course = models.ForeignKey(Course)
    def __unicode__(self):
        return str(self.course)+"-"+str(self.number)


class TeePosition(models.Model):
    color = models.ForeignKey(TeePositionColor)
    distance = models.IntegerField()
    hole = models.ForeignKey(Hole)
    def __unicode__(self):
        return str(self.hole)+"-"+self.color.color+"-"+str(self.distance)

