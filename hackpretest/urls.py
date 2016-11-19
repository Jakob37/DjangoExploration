from django.conf.urls import include, url
from django.contrib import admin

"""
This script seems to be responsible for managing
redirection of different urls to particular locations

include() - Make it easy to plug-and-play URLs (?)
Since 'polls' are in their own URLconf (polls/urls.py), they
can be placed under any 'polls' directory (matching regex),
and app will still work.

admin.site.urls is likely the administative page.
"""

# Patterns here seem to have two arguments:
#  (1) Matched pattern for incoming URL
#  (2) The target view to look for
urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'admin/', admin.site.urls),
]

