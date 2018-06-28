from django.shortcuts import render, redirect

def index(request):
    return render(request, 'survey/selection.html')

def process(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        if 'visited' not in request.session:
            request.session['visited'] = 1
        else:
            request.session['visited'] += 1
        return redirect('/results')
    else:
        return redirect('/')

def results(request):
    return render(request, 'survey/results.html')

def reset(request):
    request.session.clear()
    return redirect('/')


