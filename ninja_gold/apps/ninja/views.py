from django.shortcuts import render,redirect
import random
from time import strftime

def index(req):
    if 'gold' not in req.session:
        req.session['gold'] = 0
    if 'activities' not in req.session:
        req.session['activities'] = []
    data = {
        'gold': req.session['gold'],
        'activities': req.session['activities']
    }
    return render(req, 'ninja/game.html', data)

def process_money(req, location):
    if req.method == 'POST':
        goldEarned = 0
        activity = ''
        date = strftime("%B %d, %Y %I:%M:%S %p")
        if location == 'farm':
            goldEarned += random.randint(10,20)
        if location == 'cave':
            goldEarned += random.randint(5,10)
        if location == 'house':
            goldEarned += random.randint(2,5)
        if location == 'casino':
            goldEarned += random.randint(-50,50)
        if goldEarned >= 0:
            activity = "Earned " + str(goldEarned) + " golds from the " + location + "! (" + date + ")"
            color = 'green'
        else:
            activity = "Entered a casino and lost " + str(abs(goldEarned)) + " golds...Ouch... " + " (" + date + ")"
            color = 'red'
        listdict = req.session['activities']
        listdict.append({"content":activity, "class": color})
        req.session['activities'] = listdict
        req.session['gold'] += goldEarned
        return redirect('/')
    else:
        return redirect('/')

def reset(req):
    req.session.clear()
    return redirect('/')



# {% for x in session['activities'] %}
#    <p class='{{x.class}}'>{{x.content}}</p>
# {% endfor %}