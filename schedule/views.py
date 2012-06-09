from django.shortcuts import render_to_response, RequestContext
from schedule.models import TeeTime
from courses.models import Hole
from schedule.forms import ScoreForm
from accounts.models import Player

def index(request):
    latest_tee_time_list = TeeTime.objects.all()
    tee_time = latest_tee_time_list[0]
    holes = Hole.objects.filter(course=tee_time.course)
    return render_to_response('schedule/index.html', {'tee_time' : tee_time, 'holes':holes, 'user': request.user,})

def submit_score(request):
    latest_tee_time_list = TeeTime.objects.all()
    tee_time = latest_tee_time_list[0]
    holes = Hole.objects.filter(course=tee_time.course)
    home_players = Player.objects.filter(team=tee_time.home_team)
    away_players = Player.objects.filter(team=tee_time.away_team)

    if request.method == 'POST':
        form = ScoreForm(data=request.POST, tee_time=tee_time, course=tee_time.course, holes=holes)
        if form.is_valid(): # All validation rules pass
            form.save()
            return render_to_response('schedule/submit_score.html', {
                'form': form, 'tee_time':tee_time, 'holes':holes,
                'success_message': "Scores Added Successfully!",
                'user': request.user,
                }, context_instance=RequestContext(request),)
        else:
            error_messages = form.errors
            form = ScoreForm(tee_time=tee_time, course=tee_time.course, holes=holes)
            #intialize the form with the home team players
            form.fields['player_one'].queryset=home_players
            form.fields['player_two'].queryset=home_players
            #intitialize the form with the away team players
            form.fields['player_three'].queryset=away_players
            form.fields['player_four'].queryset=away_players
            return render_to_response('schedule/submit_score.html', {
                'form': form, 'tee_time':tee_time, 'holes':holes,
                'error_message': error_messages,
                'user': request.user,
                }, context_instance=RequestContext(request),)
    else:
        #create the form
        form = ScoreForm(tee_time=tee_time, course=tee_time.course, holes=holes)
        #initialize the fields with the home team players
        form.fields['player_one'].queryset=home_players
        form.fields['player_two'].queryset=home_players
        #intialize the fields with the away team players
        form.fields['player_three'].queryset=away_players
        form.fields['player_four'].queryset=away_players

    return render_to_response('schedule/submit_score.html', {
        'form': form, 'tee_time':tee_time, 'holes':holes, 'user': request.user,
        }, context_instance=RequestContext(request),)
