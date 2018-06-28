from django.shortcuts import render, redirect
from time import strftime, localtime

def index(req):
    if 'words' not in req.session:
        req.session['words'] = []
    data = {
        'wordlist':req.session['words']
    }
    return render(req, 'words/home.html', data)

def add_word(req):
    if 'isbig' in req.POST:
        isbig = True
    else:
        isbig = False

    temp_list = req.session['words']
    temp_list.insert(0, {'word':req.POST['word'], "color":req.POST['color'], 'isbig':isbig, 'time':strftime("%I:%M:%S %p, %B %d %Y", localtime())})
    req.session['words'] = temp_list

    return redirect('/session_words')

def clear(req):
    req.session.clear()
    return redirect('/session_words')
