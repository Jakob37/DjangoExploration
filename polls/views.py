from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone

# For latest version
# from django.urls import reverse
from django.core.urlresolvers import reverse

from .models import Question, Choice

# Create your views here.
# This seems to be 'views' related to the polls app on my site

# The ListView here seems to provide listed information
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):

        """Return the last five published questions"""
        return Question.objects.order_by('-pub_date')[:5]


# The DetailView here seems to directly retrieve template from path
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'You didn\'t select a choice',
        })
    else:
        selected_choice.votes += 1
        # Aha, we are saving directly to database
        # similarly to when using command-line previously
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

#    return HttpResponse("You're voting on question {}.".format(question_id))

def get_queryset(self):

    """
    Return the last five published questions (not including future quesitons)
    """

    return Quesion.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


