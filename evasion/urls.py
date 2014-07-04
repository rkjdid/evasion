from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/?$', 'evasion.views.home', name='home'),

    # ajax
    url(r'^contact/$', 'evasion.ajax.message', name='contact'),

    # admin
    url(r'^admin/', include(admin.site.urls)),
)


# Redirects
urlpatterns += patterns('',
    url(r'^.*', 'evasion.views.redirect', name="redirect"),
)
