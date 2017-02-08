from django.conf.urls import include, url
from django.contrib import admin

import views
admin.autodiscover()

urlpatterns = (
    url(r'^$', views.home, name='home'),
    # ajax
    url(r'^contact$', views.message, name='contact'),
    # admin
    url(r'^admin/', include(admin.site.urls)),
)
