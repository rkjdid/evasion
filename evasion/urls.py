from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# from django.template.loader import add_to_builtins
# add_to_builtins('django.templatetags.static')


urlpatterns = patterns('',
    url(r'^$', 'evasion.views.home', name='home'),
)
