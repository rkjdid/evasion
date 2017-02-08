from django.conf.urls import include, url
from django.views.generic.base import RedirectView

import web.urls

urlpatterns = [
    url(r'^works/evasion/', include(web.urls)),
    url(r'^.*', RedirectView.as_view(url='/works/evasion/')),
]
