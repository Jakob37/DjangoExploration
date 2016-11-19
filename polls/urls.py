from django.conf.urls import url

from . import views

"""
Here, we seem to have logic to redirect incomers to the poll view
This is separate from the main URL document for the page
The admin page is related to page, not poll app
"""

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

