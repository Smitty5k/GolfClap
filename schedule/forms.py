from django import forms
from accounts.models import Player
from schedule.models import Score, ScoreCard, TotalRoundScore

class ScoreForm(forms.Form):

    MAX_SCORE=10
    MIN_SCORE=1

    #Player one's data
    player_one = forms.ModelChoiceField(queryset=Player.objects.all())
    player_one_hole_one_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_one_hole_two_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_one_hole_three_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_one_hole_four_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_one_hole_five_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_one_hole_six_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_one_hole_seven_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_one_hole_eight_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_one_hole_nine_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)

    #Player two's data
    player_two = forms.ModelChoiceField(queryset=Player.objects.all())
    player_two_hole_one_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_two_hole_two_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_two_hole_three_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_two_hole_four_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_two_hole_five_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_two_hole_six_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_two_hole_seven_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_two_hole_eight_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_two_hole_nine_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)

    #Player three's data
    player_three = forms.ModelChoiceField(queryset=Player.objects.all())
    player_three_hole_one_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_three_hole_two_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_three_hole_three_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_three_hole_four_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_three_hole_five_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_three_hole_six_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_three_hole_seven_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_three_hole_eight_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_three_hole_nine_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)

    #Player four's data
    player_four = forms.ModelChoiceField(queryset=Player.objects.all())
    player_four_hole_one_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_four_hole_two_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_four_hole_three_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_four_hole_four_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_four_hole_five_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_four_hole_six_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_four_hole_seven_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_four_hole_eight_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)
    player_four_hole_nine_score = forms.IntegerField(initial=0, max_value=MAX_SCORE, min_value=MIN_SCORE)

    def __init__(self, tee_time, course, holes, *args, **kwargs):
        super(ScoreForm, self).__init__(*args, **kwargs)
        self.tee_time=tee_time
        self.course=course
        self.holes=holes

    def save_player_one_scores(self, score_card, commit=True):
        """
            Processes the scores for the player. Uses get_or_create score to prevent
            duplciation if the form is updated after the scores are created.
        """
        #Get the player
        player_one=self.cleaned_data["player_one"]
        #Score One
        score_one, created = Score.objects.get_or_create(hole=self.holes[0],
            player=player_one, score_card=score_card, tee_time=score_card.tee_time)
        score_one.score=self.cleaned_data["player_one_hole_one_score"]
        #Score Two
        score_two, created = Score.objects.get_or_create(hole=self.holes[1],
            player=player_one, score_card=score_card, tee_time=score_card.tee_time)
        score_two.score=self.cleaned_data["player_one_hole_two_score"]
        #Score Three
        score_three, created = Score.objects.get_or_create(hole=self.holes[2],
            player=player_one, score_card=score_card, tee_time=score_card.tee_time)
        score_three.score=self.cleaned_data["player_one_hole_three_score"]
        #Score Four
        score_four, created = Score.objects.get_or_create(hole=self.holes[3],
            player=player_one, score_card=score_card, tee_time=score_card.tee_time)
        score_four.score=self.cleaned_data["player_one_hole_four_score"]
        #Score Five
        score_five, created = Score.objects.get_or_create(hole=self.holes[4],
            player=player_one, score_card=score_card, tee_time=score_card.tee_time)
        score_five.score=self.cleaned_data["player_one_hole_five_score"]
        #Score Six
        score_six, created=Score.objects.get_or_create(hole=self.holes[5],
            player=player_one, score_card=score_card, tee_time=score_card.tee_time)
        score_six.score=self.cleaned_data["player_one_hole_six_score"]
        #Score Seven
        score_seven, created=Score.objects.get_or_create(hole=self.holes[6],
            player=player_one, score_card=score_card, tee_time=score_card.tee_time)
        score_seven.score=self.cleaned_data["player_one_hole_seven_score"]
        #Score Eight
        score_eight, created=Score.objects.get_or_create(hole=self.holes[7],
            player=player_one, score_card=score_card, tee_time=score_card.tee_time)
        score_eight.score=self.cleaned_data["player_one_hole_eight_score"]
        #Score Nine
        score_nine, created=Score.objects.get_or_create(hole=self.holes[8],
            player=player_one, score_card=score_card, tee_time=score_card.tee_time)
        score_nine.score=self.cleaned_data["player_one_hole_nine_score"]
        #Total
        total_round_score, created=TotalRoundScore.objects.get_or_create(
            player=player_one, score_card=score_card, tee_time=score_card.tee_time)
        total_round_score.total_score=score_one.score+score_two.score+score_three.score+score_four.score+score_five.score+score_six.score+score_seven.score+score_eight.score+score_nine.score
        #totalscore=score_one.score+score_two.score+score_three.score+score_four.score+score_five.score+score_six.score+score_seven.score+score_eight.score+score_nine.score



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
            total_round_score.save()

    def save_player_two_scores(self, score_card, commit=True):
        """
            Processes the scores for the player. Uses get_or_create score to prevent
            duplciation if the form is updated after the scores are created.
        """
        #Get the player
        player_two=self.cleaned_data["player_two"]
        #Score one
        score_one, created = Score.objects.get_or_create(hole=self.holes[0],
            player=player_two, score_card=score_card, tee_time=score_card.tee_time)
        score_one.score=self.cleaned_data["player_two_hole_one_score"]
        #Score Two
        score_two, created = Score.objects.get_or_create(hole=self.holes[1],
            player=player_two, score_card=score_card, tee_time=score_card.tee_time)
        score_two.score=self.cleaned_data["player_two_hole_two_score"]
        #Score Three
        score_three, created = Score.objects.get_or_create(hole=self.holes[2],
            player=player_two, score_card=score_card, tee_time=score_card.tee_time)
        score_three.score=self.cleaned_data["player_two_hole_three_score"]
        #Score Four
        score_four, created = Score.objects.get_or_create(hole=self.holes[3],
            player=player_two, score_card=score_card, tee_time=score_card.tee_time)
        score_four.score=self.cleaned_data["player_two_hole_four_score"]
        #Score Five
        score_five, created = Score.objects.get_or_create(hole=self.holes[4],
            player=player_two, score_card=score_card, tee_time=score_card.tee_time)
        score_five.score=self.cleaned_data["player_two_hole_five_score"]
        #Score Six
        score_six, created=Score.objects.get_or_create(hole=self.holes[5],
            player=player_two, score_card=score_card, tee_time=score_card.tee_time)
        score_six.score=self.cleaned_data["player_two_hole_six_score"]
        #Score Seven
        score_seven, created=Score.objects.get_or_create(hole=self.holes[6],
            player=player_two, score_card=score_card, tee_time=score_card.tee_time)
        score_seven.score=self.cleaned_data["player_two_hole_seven_score"]
        #Score Eight
        score_eight, created=Score.objects.get_or_create(hole=self.holes[7],
            player=player_two, score_card=score_card, tee_time=score_card.tee_time)
        score_eight.score=self.cleaned_data["player_two_hole_eight_score"]
        #Score Nine
        score_nine, created=Score.objects.get_or_create(hole=self.holes[8],
            player=player_two, score_card=score_card, tee_time=score_card.tee_time)
        score_nine.score=self.cleaned_data["player_two_hole_nine_score"]
        #Total
        total_round_score, created=TotalRoundScore.objects.get_or_create(
            player=player_two, score_card=score_card, tee_time=score_card.tee_time)
        total_round_score.total_score=score_one.score+score_two.score+score_three.score+score_four.score+score_five.score+score_six.score+score_seven.score+score_eight.score+score_nine.score



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
            total_round_score.save()


    def save_player_three_scores(self, score_card, commit=True):
        """
            Processes the scores for the player. Uses get_or_create score to prevent
            duplciation if the form is updated after the scores are created.
        """
        #Get the player
        player_three=self.cleaned_data["player_three"]
        #Score one
        score_one, created = Score.objects.get_or_create(hole=self.holes[0],
            player=player_three, score_card=score_card, tee_time=score_card.tee_time)
        score_one.score=self.cleaned_data["player_three_hole_one_score"]
        #Score Two
        score_two, created = Score.objects.get_or_create(hole=self.holes[1],
            player=player_three, score_card=score_card, tee_time=score_card.tee_time)
        score_two.score=self.cleaned_data["player_three_hole_two_score"]
        #Score Three
        score_three, created = Score.objects.get_or_create(hole=self.holes[2],
            player=player_three, score_card=score_card, tee_time=score_card.tee_time)
        score_three.score=self.cleaned_data["player_three_hole_three_score"]
        #Score Four
        score_four, created = Score.objects.get_or_create(hole=self.holes[3],
            player=player_three, score_card=score_card, tee_time=score_card.tee_time)
        score_four.score=self.cleaned_data["player_three_hole_four_score"]
        #Score Five
        score_five, created = Score.objects.get_or_create(hole=self.holes[4],
            player=player_three, score_card=score_card, tee_time=score_card.tee_time)
        score_five.score=self.cleaned_data["player_three_hole_five_score"]
        #Score Six
        score_six, created=Score.objects.get_or_create(hole=self.holes[5],
            player=player_three, score_card=score_card, tee_time=score_card.tee_time)
        score_six.score=self.cleaned_data["player_three_hole_six_score"]
        #Score Seven
        score_seven, created=Score.objects.get_or_create(hole=self.holes[6],
            player=player_three, score_card=score_card, tee_time=score_card.tee_time)
        score_seven.score=self.cleaned_data["player_three_hole_seven_score"]
        #Score Eight
        score_eight, created=Score.objects.get_or_create(hole=self.holes[7],
            player=player_three, score_card=score_card, tee_time=score_card.tee_time)
        score_eight.score=self.cleaned_data["player_three_hole_eight_score"]
        #Score Nine
        score_nine, created=Score.objects.get_or_create(hole=self.holes[8],
            player=player_three, score_card=score_card, tee_time=score_card.tee_time)
        score_nine.score=self.cleaned_data["player_three_hole_nine_score"]
        #Total
        total_round_score, created=TotalRoundScore.objects.get_or_create(
            player=player_three, score_card=score_card, tee_time=score_card.tee_time)
        total_round_score.total_score=score_one.score+score_two.score+score_three.score+score_four.score+score_five.score+score_six.score+score_seven.score+score_eight.score+score_nine.score

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
            total_round_score.save()

    def save_player_four_scores(self, score_card, commit=True):
        """
            Processes the scores for the player. Uses get_or_create score to prevent
            duplciation if the form is updated after the scores are created.
        """
        #Get the player
        player_four=self.cleaned_data["player_four"]
        #Score one
        score_one, created = Score.objects.get_or_create(hole=self.holes[0],
            player=player_four, score_card=score_card, tee_time=score_card.tee_time)
        score_one.score=self.cleaned_data["player_four_hole_one_score"]
        #Score Two
        score_two, created = Score.objects.get_or_create(hole=self.holes[1],
            player=player_four, score_card=score_card, tee_time=score_card.tee_time)
        score_two.score=self.cleaned_data["player_four_hole_two_score"]
        #Score Three
        score_three, created = Score.objects.get_or_create(hole=self.holes[2],
            player=player_four, score_card=score_card, tee_time=score_card.tee_time)
        score_three.score=self.cleaned_data["player_four_hole_three_score"]
        #Score Four
        score_four, created = Score.objects.get_or_create(hole=self.holes[3],
            player=player_four, score_card=score_card, tee_time=score_card.tee_time)
        score_four.score=self.cleaned_data["player_four_hole_four_score"]
        #Score Five
        score_five, created = Score.objects.get_or_create(hole=self.holes[4],
            player=player_four, score_card=score_card, tee_time=score_card.tee_time)
        score_five.score=self.cleaned_data["player_four_hole_five_score"]
        #Score Six
        score_six, created=Score.objects.get_or_create(hole=self.holes[5],
            player=player_four, score_card=score_card, tee_time=score_card.tee_time)
        score_six.score=self.cleaned_data["player_four_hole_six_score"]
        #Score Seven
        score_seven, created=Score.objects.get_or_create(hole=self.holes[6],
            player=player_four, score_card=score_card, tee_time=score_card.tee_time)
        score_seven.score=self.cleaned_data["player_four_hole_seven_score"]
        #Score Eight
        score_eight, created=Score.objects.get_or_create(hole=self.holes[7],
            player=player_four, score_card=score_card, tee_time=score_card.tee_time)
        score_eight.score=self.cleaned_data["player_four_hole_eight_score"]
        #Score Nine
        score_nine, created=Score.objects.get_or_create(hole=self.holes[8],
            player=player_four, score_card=score_card, tee_time=score_card.tee_time)
        score_nine.score=self.cleaned_data["player_four_hole_nine_score"]
        #Total
        total_round_score, created=TotalRoundScore.objects.get_or_create(
            player=player_four, score_card=score_card, tee_time=score_card.tee_time)
        total_round_score.total_score=score_one.score+score_two.score+score_three.score+score_four.score+score_five.score+score_six.score+score_seven.score+score_eight.score+score_nine.score

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
            total_round_score.save()

    def save(self, commit=True):

        score_card, created_score_card = ScoreCard.objects.get_or_create(tee_time=self.tee_time, course=self.course)

        if commit:
            #only save the score card if it's new
            if created_score_card:
                score_card.save()

        self.save_player_one_scores(score_card)
        self.save_player_two_scores(score_card)
        self.save_player_three_scores(score_card)
        self.save_player_four_scores(score_card)


        return score_card