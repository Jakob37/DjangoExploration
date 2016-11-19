from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Question

# Create your views here.

# This seems to be 'views' related to the polls app on my site

def index(request):

    print(request)

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

# Original
#    return HttpResponse(template.render(context, request))


def detail(request, question_id):

#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#    return render(request, 'polls/detail.html', {'question': question})

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question {}"
    return HttpResponse(response.format(question_id))


def vote(request, question_id):
    return HttpResponse("You're voting on question {}.".format(question_id))



