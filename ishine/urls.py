from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from ishine.settings import TEMPLATE_DIRS

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ishine.views.home', name='home'),
    # url(r'^ishine/', include('ishine.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^blog/', include('blog.urls')),
    #(r'^login/$', 'django.contrib.auth.views.login'),
)
