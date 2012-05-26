from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from leagues.models import League

# Create your models here.
class Team(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=25)
    league = models.ForeignKey(League)
    def __unicode__(self):
        return str(self.number)+'-'+self.name

    class Meta:
        unique_together = (('number', 'name'),)

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', related_name='profile')
    displayName = models.CharField(max_length=100)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    def __unicode__(self):
        return self.displayName

    signals.post_save.connect(create_user_profile, sender=User)

#Class For Representing a Player
class Player(models.Model):
    name = models.CharField(max_length=100)
    handicap = models.IntegerField()
    team = models.ForeignKey(Team)
    user = models.ForeignKey(UserProfile)

    def __unicode__(self):
        return self.name