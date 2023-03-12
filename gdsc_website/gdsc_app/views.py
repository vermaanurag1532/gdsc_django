from django.shortcuts import render
from .models import Our_Activities, Events, Club_Coordinators, CoreTeam

# Create your views here.


def index(request):
    context = {}
    context['our_activities'] = Our_Activities.objects.all()
    context['events'] = Events.objects.all()
    context['club_coordinator'] = Club_Coordinators.objects.all()
    context['coreTeams'] = CoreTeam.objects.all()

    return render(request, 'gdsc_app/index.html', context)
