from django.db import models

# Create your models here.
class League(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Season(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    league = models.ForeignKey(League)

    def __unicode__(self):
        return str(self.league)+'-'+str(self.start_date)
