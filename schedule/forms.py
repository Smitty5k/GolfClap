from django import forms
from accounts.models import Player
from schedule.models import Score, ScoreCard

class ScoreForm(forms.Form):

    MAX_SCORE=10
    MIN_SCORE=1

    def __init__(self, tee_time, course, holes, *args, **kwargs):
        super(ScoreForm, self).__init__(*args, **kwargs)
        self.tee_time=tee_time
        self.course=course
        self.holes=holes
    #Player one's data
    player_one = forms.ModelChoiceField(queryset=Player.objects.all())
    player_one_hole_one_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_one_hole_two_score = forms.IntegerField(initial=0)
    player_one_hole_three_score = forms.IntegerField(initial=0)
    player_one_hole_four_score = forms.IntegerField(initial=0)
    player_one_hole_five_score = forms.IntegerField(initial=0)
    player_one_hole_six_score = forms.IntegerField(initial=0)
    player_one_hole_seven_score = forms.IntegerField(initial=0)
    player_one_hole_eight_score = forms.IntegerField(initial=0)
    player_one_hole_nine_score = forms.IntegerField(initial=0)

    #Player two's data
    player_two = forms.ModelChoiceField(queryset=Player.objects.all())
    player_two_hole_one_score = forms.IntegerField(initial=0)
    player_two_hole_two_score = forms.IntegerField(initial=0)
    player_two_hole_three_score = forms.IntegerField(initial=0)
    player_two_hole_four_score = forms.IntegerField(initial=0)
    player_two_hole_five_score = forms.IntegerField(initial=0)
    player_two_hole_six_score = forms.IntegerField(initial=0)
    player_two_hole_seven_score = forms.IntegerField(initial=0)
    player_two_hole_eight_score = forms.IntegerField(initial=0)
    player_two_hole_nine_score = forms.IntegerField(initial=0)

    #Player three's data
    player_three = forms.ModelChoiceField(queryset=Player.objects.all())
    player_three_hole_one_score = forms.IntegerField(initial=0)
    player_three_hole_two_score = forms.IntegerField(initial=0)
    player_three_hole_three_score = forms.IntegerField(initial=0)
    player_three_hole_four_score = forms.IntegerField(initial=0)
    player_three_hole_five_score = forms.IntegerField(initial=0)
    player_three_hole_six_score = forms.IntegerField(initial=0)
    player_three_hole_seven_score = forms.IntegerField(initial=0)
    player_three_hole_eight_score = forms.IntegerField(initial=0)
    player_three_hole_nine_score = forms.IntegerField(initial=0)

    #Player four's data
    player_four = forms.ModelChoiceField(queryset=Player.objects.all())
    player_four_hole_one_score = forms.IntegerField(initial=0)
    player_four_hole_two_score = forms.IntegerField(initial=0)
    player_four_hole_three_score = forms.IntegerField(initial=0)
    player_four_hole_four_score = forms.IntegerField(initial=0)
    player_four_hole_five_score = forms.IntegerField(initial=0)
    player_four_hole_six_score = forms.IntegerField(initial=0)
    player_four_hole_seven_score = forms.IntegerField(initial=0)
    player_four_hole_eight_score = forms.IntegerField(initial=0)
    player_four_hole_nine_score = forms.IntegerField(initial=0)


#    def clean(self):
#        for name, field in self.fields.items():
#            pattern = "player_(?:[a-z][a-z]+)_hole_"
#            prog = re.compile(pattern)
#            if(prog.match(name)):
#                value = getattr(self, name)
#            else:
#                pass;
        #cleaned_data = self.cleaned_data
        #cleaned_data['real_field'] = cleaned_data['virtual_field']
        #return cleaned_data

    #def clean_player_one_hole_one_score:


    def save_player_one_scores(self, score_card, commit=True):
        player_one=self.cleaned_data["player_one"]
        score_one = Score.objects.create(hole=self.holes[0],
            score=self.cleaned_data["player_one_hole_one_score"],
            player=player_one, score_card=score_card)
        score_two = Score.objects.create(hole=self.holes[1],
            score=self.cleaned_data["player_one_hole_two_score"],
            player=player_one, score_card=score_card)
        score_three =Score.objects.create(hole=self.holes[2],
            score=self.cleaned_data["player_one_hole_three_score"],
            player=player_one, score_card=score_card)
        score_four =Score.objects.create(hole=self.holes[3],
            score=self.cleaned_data["player_one_hole_four_score"],
            player=player_one, score_card=score_card)
        score_five =Score.objects.create(hole=self.holes[4],
            score=self.cleaned_data["player_one_hole_five_score"],
            player=player_one, score_card=score_card)
        score_six =Score.objects.create(hole=self.holes[5],
            score=self.cleaned_data["player_one_hole_six_score"],
            player=player_one, score_card=score_card)
        score_seven =Score.objects.create(hole=self.holes[6],
            score=self.cleaned_data["player_one_hole_seven_score"],
            player=player_one, score_card=score_card)
        score_eight =Score.objects.create(hole=self.holes[7],
            score=self.cleaned_data["player_one_hole_eight_score"],
            player=player_one, score_card=score_card)
        score_nine =Score.objects.create(hole=self.holes[8],
            score=self.cleaned_data["player_one_hole_nine_score"],
            player=player_one, score_card=score_card)


        if commit:
            score_one.save()
            score_two.save()
            score_three.save()
            score_four.save()
            score_five.save()
            score_six.save()
            score_seven.save()
            score_eight.save()
            score_nine.save()


    def save(self, commit=True):

        score_card, created = ScoreCard.objects.get_or_create(tee_time=self.tee_time, course=self.course)

        if commit:
            if created:
                score_card.save()
            self.save_player_one_scores(score_card)
            return score_card