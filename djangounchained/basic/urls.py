from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'djangounchained.basic.views.basic_home', name='home'),
    url(r'^home$', 'djangounchained.basic.views.basic_home', name='home'),
    url(r'^login$', 'djangounchained.basic.views.basic_login', name='login'),
    url(r'^logout$', 'djangounchained.basic.views.basic_logout', name='logout'),    
)
