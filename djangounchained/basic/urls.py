from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'djangounchained.basic.views.home', name='home'),
    url(r'^home$', 'djangounchained.basic.views.home', name='home'),
    url(r'^login$', 'djangounchained.basic.views.login', name='login'),
)
