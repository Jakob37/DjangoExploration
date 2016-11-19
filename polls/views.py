from django.http import HttpResponse

# Create your views here.

# This seems to be 'views' related to the polls app on my site

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


