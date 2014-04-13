from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db.models import Q
import random

from dvc.models import Fighter, Warcategory, Prompt, Battle, Face

# Create your views here.
def index(request):
    request.session['warcategory_id'] = 1
    request.session['round'] = 1
    request.session['wins'] = 0
    return render(request, 'dvc/index.html', {})



def fight(request):
    prompts = Prompt.objects.all()
    prompt = random.choice(prompts)
    warcategory = Warcategory.objects.get(pk=request.session['warcategory_id'])
    fighters_list = [warcategory.challenger, warcategory.challenged]
    error_message = None
    images = [random.choice(Face.objects.filter(fighter=warcategory.challenger)), random.choice(Face.objects.filter(fighter=warcategory.challenged))]
    
    
    return render(request, 'dvc/fight.html',
                  {'prompt':prompt,
                   'error_message':error_message,
                   'fighters_list':fighters_list,
                   'round': request.session['round'],
                   'images': images,
                   })



def about(request):
    return render(request, 'dvc/about.html', {})



def results(request):
    warcategory = Warcategory.objects.get(pk=request.session['warcategory_id'])
    challenger = warcategory.challenger
    challenged = warcategory.challenged
    wins = 0
    battles = Battle.objects.filter(warcategory=warcategory.id)
    for battle in battles:
        if battle.winner == challenger:
            wins = wins + 1

    if (request.session['wins'] > 1):
        text = challenger.name + " wins"
    else:
        text = challenger.name + " loses"

    image = random.choice(Face.objects.filter(fighter=warcategory.challenger))
    return render(request, 'dvc/results.html',
                  {'challenger':challenger,
                   'challenged':challenged,
                   'session': request.session['wins'],
                   'text':text,
                   'imagepath':image.path,
                   'total': battles.count(),
                   'wins':wins
                   })



def fighters(request):
    fighters_list = Fighter.objects.all().order_by('-name')
    return render(request, 'dvc/fighters.html',
                  {'fighters_list': fighters_list})



def vote(request, prompt_id):
    p = get_object_or_404(Prompt, pk=prompt_id)
    fightround = request.session['round'] + 1;
    request.session['round'] = fightround
    try:
        selected_choice = Fighter.objects.get(pk=request.POST['winner'])
    except (KeyError, Fighter.DoesNotExist):
        fighters_list = Fighter.objects.all().order_by('-name')
        return render(request, 'dvc/fight.html', {
            'prompt':p,
            'error_message': "You didn't select a valid choice.",
            'fighters_list':fighters_list,
        })
    else:
        battle = Battle()
        warcategory = Warcategory.objects.get(pk=request.session['warcategory_id'])
        battle.winner = selected_choice
        if selected_choice == warcategory.challenger:
            request.session['wins'] += 1
        battle.warcategory = warcategory
        battle.prompt = p
        battle.create_time = timezone.now()
        battle.save()
        
        if(fightround > 3):
            #need to use responseredirect in case user hits back
            return HttpResponseRedirect(reverse('dvc:results'))
        else:
            return HttpResponseRedirect(reverse('dvc:fight'))
    
    
    