from django.shortcuts import render_to_response, redirect, render
from django.template.context import RequestContext


def home(request):
    return render_to_response(
        '0.home.html',
        context_instance=RequestContext(request)
    )