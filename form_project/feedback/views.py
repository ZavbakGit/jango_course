from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import FeedBackForm
from .models import Feedback
from django.views import View
from django.views.generic.base import TemplateView


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


class DoneView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test'] = 'Ура'
        return context

    template_name = 'feedback/done.html'


class DetailFeedBack(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        feedback = get_object_or_404(Feedback, id=kwargs['id_fb'])
        context['feedback'] = feedback
        return context

    template_name = 'feedback/detail_feedback.html'


class ListFeedBack(TemplateView):
    def get_context_data(self, **kwargs):
        feedbacks = Feedback.objects.all()

        context = super().get_context_data(**kwargs)
        context['feedbacks'] = feedbacks
        return context

    template_name = 'feedback/list_feedback.html'


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
