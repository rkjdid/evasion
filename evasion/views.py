from django.shortcuts import render_to_response, redirect as _redirect
from django.template.context import RequestContext

def home(request):

  params = {}

  return render_to_response(
      '0.home.html',
      params,
      context_instance=RequestContext(request)
  )

def redirect(request, url="/"):
  return _redirect(url, context_instance=RequestContext)