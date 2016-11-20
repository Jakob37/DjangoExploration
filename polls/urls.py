from django.conf.urls import url

from . import views

"""
Here, we seem to have logic to redirect incomers to the poll view
This is separate from the main URL document for the page
The admin page is related to page, not poll app
"""

# We seem to be generalizing the details and results views
# Not sure about the procedure here yet

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

