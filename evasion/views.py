from django.shortcuts import render_to_response, redirect, render
from django.template.context import RequestContext

from django.conf import settings

def home(request):

  params = {}

  return render_to_response(
      '0.home.html',
      params,
      context_instance=RequestContext(request)
  )