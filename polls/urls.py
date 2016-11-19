from django.conf.urls import url

from . import views

"""
Here, we seem to have logic to redirect incomers to the poll view
This is separate from the main URL document for the page
The admin page is related to page, not poll app
"""
app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

