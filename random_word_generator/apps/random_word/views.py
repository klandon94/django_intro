from django.shortcuts import render,redirect
from django.utils.crypto import get_random_string

def index(req):
    if 'increment' not in req.session:
            req.session['increment'] = 1
    data={
        'random': get_random_string(length=14),
        'attempt': req.session['increment']
    }
    return render(req,'random_word/index.html',data)

def increment(req):
    if req.method == 'POST':
        req.session['increment'] += 1
        return redirect('/random_word')
    else:
        return redirect('/random_word')

def reset(req):
    req.session.clear()
    return redirect('/random_word')
