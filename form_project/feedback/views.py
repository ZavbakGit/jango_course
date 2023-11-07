from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import FeedBackForm
from .models import Feedback
from django.views import View


class FeedBackView(View):
    def get(self, request):
        form = FeedBackForm()

        return render(request, 'feedback/feedback.html', context={
            'form': form
        })

    def post(self, request):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')

        return render(request, 'feedback/feedback.html', context={
            'form': form
        })


class DoneView(View):
    def get(self, request):
        return render(request, 'feedback/done.html')


class FeedBackUpdateView(View):
    def get(self, request, id_feedback):
        # feed = Feedback.objects.get(id=id_feedback)
        feed = get_object_or_404(Feedback, pk=id_feedback)

        form = FeedBackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={
            'form': form
        })

    def post(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedBackForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/{id_feedback}')
        else:
            return render(request, 'feedback/feedback.html', context={
                'form': form
            })


def done(request):
    return render(request, 'feedback/done.html')


def index(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            # feed = Feedback(
            #     name=form.cleaned_data['name'],
            #     surname=form.cleaned_data['surname'],
            #     rating=form.cleaned_data['rating'],
            #     feedback=form.cleaned_data['feedback'],
            # )
            form.save()
            return HttpResponseRedirect('/done')
    else:
        form = FeedBackForm()

    return render(request, 'feedback/feedback.html', context={
        'form': form
    })


def update_feedback(request, id_feedback: int):
    feed = Feedback.objects.get(id=id_feedback)
    if request.method == 'POST':
        form = FeedBackForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/{id_feedback}')
    else:
        form = FeedBackForm(instance=feed)

    return render(request, 'feedback/feedback.html', context={
        'form': form
    })
