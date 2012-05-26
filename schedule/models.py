from django.db import models
from leagues.models import Season
from accounts.models import Team, Player
from courses.models import Hole, Course

# Create your models here.
class TeeTime(models.Model):
    week = models.DateField()
    time = models.TimeField()
    season = models.ForeignKey(Season)
    home_team = models.ForeignKey(Team, related_name='home_team')
    away_team = models.ForeignKey(Team, related_name='away_team')
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return str(self.week)+"-"+str(self.home_team)+"-"+str(self.away_team)


class ScoreCard(models.Model):
    tee_time = models.ForeignKey(TeeTime)
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return str(self.tee_time)+"-"+str(self.course)


class Score(models.Model):
    score_card = models.ForeignKey(ScoreCard)
    hole = models.ForeignKey(Hole)
    player = models.ForeignKey(Player)
    score = models.IntegerField()

    def __unicode__(self):
        return str(self.score_card)+"-"+str(self.hole)+"-"+str(self.player)
