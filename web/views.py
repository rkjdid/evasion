# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect as _redirect
from django.template.context import RequestContext
from django.http import HttpResponse

import datetime, pytz, json, logging
import models, tracer
from evasion import settings


def home(request):
  try:
    tracer.trace_user(request)
  except Exception as e:
    log = logging.getLogger('django.request')
    log.exception("Error tracing user: %s" % e)

  return render_to_response(
      'web/0.home.html',
      context=RequestContext(request)
  )

#------#
# AJAX #
#------#

def message(request):
  m = models.Message()
  m.date_filled = True
  m.date_message = datetime.datetime.now(tz=pytz.timezone(settings.TIME_ZONE))

  # crop values to match database's max_lengths
  m.email = request.GET['email'][:models.Message._meta.get_field('email').max_length]
  m.lastname = request.GET['lastname'][:models.Message._meta.get_field('lastname').max_length]
  m.firstname = request.GET['firstname'][:models.Message._meta.get_field('firstname').max_length]
  m.phone = request.GET['phone'][:models.Message._meta.get_field('phone').max_length]
  m.message = request.GET['message']

  v = None
  try:
    v = tracer.trace_user(request)
  except Exception as e:
    log = logging.getLogger('django.request')
    log.exception("Error tracing user: %s" % e)
  m.visitor = v

  try:
    m.date_reservation = datetime.datetime.strptime(request.GET['date'], '%d/%m/%Y')
  except:
    m.date_reservation = datetime.datetime.today()
    m.date_filled = False
  m.save() # allow m.id to be available

  try:
    m.message_sent = m.send()
  except Exception:
    m.message_sent = False
    log = logging.getLogger('django.request')
    log.exception("Couldn't send e-mail (message #%s)" % m.id)
  m.save()

  json_data = dict()
  json_data['result'] = \
    u'Merci de votre message <em>%s</em>, vous recevrez notre réponse dans les plus brefs délais.<br><br>' % unicode(m.firstname) +\
    u'N\'hésitez pas à vous balader sur notre page ' + \
    u'<a href=\'https://www.facebook.com/evasionantillaise\' target=\'_blank\'>Facebook</a>, ' +\
    u'et si nous avons le plaisir de vous accueillir, à y laisser un petit mot ou partager autour ' +\
    u'de vous !<br><br>À très bientôt'
  json_data = json.dumps(json_data)

  response = HttpResponse(json_data, content_type='application/json')
  response['Content-Length'] = len(json_data)

  return response

def redirect(request, url="/"):
  return _redirect(url, context=RequestContext)


