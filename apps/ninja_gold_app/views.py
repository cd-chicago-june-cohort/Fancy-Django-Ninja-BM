from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import random 
from time import strftime, localtime, ctime

def index(request):

    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []

    return render(request, 'ninja_gold_app/index.html')

#-----------------------------------------------------------------------

def process_money(request):

    if request.POST['building']=='farm':
        print "farm"
        request.session['newgold'] = random.randint(10,21)
        request.session['gold'] += request.session['newgold']
        gold = request.session['gold']
        print gold
        activities=request.session['activities']
        activities.insert(0,"You just farmed your way to " + str(request.session['newgold']) +  " gold on " + ctime())
        request.session['activities']=activities
        print activities
        return redirect('/')

    elif request.POST['building']=='cave':
        print "cave"
        request.session['newgold'] = random.randint(5,11)
        request.session['gold'] += request.session['newgold']
        gold = request.session['gold']
        print gold
        activities=request.session['activities']
        activities.insert(0,"You just found " + str(request.session['newgold']) + " Gold in a cave on " + ctime())
        request.session['activities']=activities
        return redirect('/')

    elif request.POST['building']=='house':
        print "house"
        request.session['newgold'] = random.randint(5,11)
        request.session['gold'] += request.session['newgold']
        gold = request.session['gold']
        print gold
        activities=request.session['activities']
        activities.insert(0,"A house fell on you, collect " + str(request.session['newgold']) + " Gold on " + ctime())
        request.session['activities']=activities
        return redirect('/')

    elif request.POST['building']=='casino':
        print "casino"
        request.session['newgold'] = random.randint(-50,50)
        request.session['gold'] += request.session['newgold']
        gold = request.session['gold']
        print gold
        activities=request.session['activities']
        if request.session['newgold'] < 0:
            activities.insert(0,"You just lost " + str(request.session['newgold']) + " Gold at the Casino on " + ctime())
        else: 
            activities.insert(0,"You just won " + str(request.session['newgold']) + " Gold at the Casino on " + ctime())
    
        request.session['activities']=activities
        
        if gold < 0:
            activities.insert(0,"You outta cash, FOOL.")
            return redirect('/reset')
        return redirect('/')

def reset(request):

    request.session.flush()
    return redirect('/')