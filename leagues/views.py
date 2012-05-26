from django.shortcuts import render_to_response
from leagues.models import League

def index(request):
    latest_league_list = League.objects.all().order_by('-name')[:5]
    return render_to_response('leagues/index.html', {'latest_league_list': latest_league_list})