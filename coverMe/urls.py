from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oweMe.views.home', name='home'),
    # url(r'^oweMe/', include('oweMe.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', "coverMe.views.index"),
    url(r'^login/$', 'users.views.login', name="login"),
    url(r'^register/$', 'users.views.register', name="register"),
    url(r'^logout/$', 'users.views.logout', name="logout"),

)
