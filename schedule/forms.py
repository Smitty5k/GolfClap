from django import forms
from accounts.models import Player
from schedule.models import Score, ScoreCard, TeeTime
from courses.models import Course, Hole

class ScoreForm(forms.Form):

    def __init__(self, tee_time, course, holes, *args, **kwargs):
        super(ScoreForm, self).__init__(*args, **kwargs)
        self.tee_time=tee_time
        self.course=course
        self.holes=holes

    player_one = forms.ModelChoiceField(queryset=Player.objects.all())
    player_one_hole_one_score = forms.IntegerField()
    player_one_hole_two_score = forms.IntegerField()
    player_one_hole_three_score = forms.IntegerField()
    player_one_hole_four_score = forms.IntegerField()
    player_one_hole_five_score = forms.IntegerField()
    player_one_hole_six_score = forms.IntegerField()
    player_one_hole_seven_score = forms.IntegerField()
    player_one_hole_eight_score = forms.IntegerField()
    player_one_hole_nine_score = forms.IntegerField()

    player_two = forms.ModelChoiceField(queryset=Player.objects.all())
    player_two_hole_one_score = forms.IntegerField()
    player_two_hole_two_score = forms.IntegerField()
    player_two_hole_three_score = forms.IntegerField()
    player_two_hole_four_score = forms.IntegerField()
    player_two_hole_five_score = forms.IntegerField()
    player_two_hole_six_score = forms.IntegerField()
    player_two_hole_seven_score = forms.IntegerField()
    player_two_hole_eight_score = forms.IntegerField()
    player_two_hole_nine_score = forms.IntegerField()

    player_three = forms.ModelChoiceField(queryset=Player.objects.all())
    player_three_hole_one_score = forms.IntegerField()
    player_three_hole_two_score = forms.IntegerField()
    player_three_hole_three_score = forms.IntegerField()
    player_three_hole_four_score = forms.IntegerField()
    player_three_hole_five_score = forms.IntegerField()
    player_three_hole_six_score = forms.IntegerField()
    player_three_hole_seven_score = forms.IntegerField()
    player_three_hole_eight_score = forms.IntegerField()
    player_three_hole_nine_score = forms.IntegerField()

    player_four = forms.ModelChoiceField(queryset=Player.objects.all())
    player_four_hole_one_score = forms.IntegerField()
    player_four_hole_two_score = forms.IntegerField()
    player_four_hole_three_score = forms.IntegerField()
    player_four_hole_four_score = forms.IntegerField()
    player_four_hole_five_score = forms.IntegerField()
    player_four_hole_six_score = forms.IntegerField()
    player_four_hole_seven_score = forms.IntegerField()
    player_four_hole_eight_score = forms.IntegerField()
    player_four_hole_nine_score = forms.IntegerField()

    def save(self, commit=True):
        score_card = ScoreCard.objects.create(tee_time=self.tee_time, course=self.course)
        #user = User.objects.create_user(self.cleaned_data["username"], self.cleaned_data["email"], self.cleaned_data["password1"])
        #user.is_active=False;
        if commit:
            #score_card.save()
            #save_player_one_scores(score_card)
            return score_card

    #def save_player_one_scores(self, score_card, commit=True):
        #pass
        #score = Score.objects.create(hole=hole_one, score=player_one_hole_one_score, player=player_one, score_card=score_card)
        #if commit:
        #    score.save()
        #holes = self.holes
        #score_card = score_card
        #hole_one = self.cleaned_data['']
        #player = self.cleaned_data["player_one"]
        #score =