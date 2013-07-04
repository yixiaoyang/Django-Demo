from django.conf.urls.defaults import *
from blog.views import archive, user_login
from ishine.settings import TEMPLATE_DIRS
import os

_path = os.path.dirname(globals()["__file__"])

urlpatterns = patterns('',
    # add bootstrap surpport
    (r'^login/bootstrap/*(?P<path>.*)$', 'django.views.static.serve', {'document_root':TEMPLATE_DIRS[0]+'/bootstrap'}),
    (r'^articles/$', archive),
    (r'^login/$', user_login),
)
