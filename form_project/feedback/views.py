from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedBackForm


# Create your views here.

def done(request):
    return render(request, 'feedback/done.html')


def index(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/done')
    else:
        form = FeedBackForm()
    return render(request, 'feedback/feedback.html', context={
        'form': form
    })
