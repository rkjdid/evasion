# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
import datetime, pytz

import models, settings

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

  try:
    m.date_reservation = datetime.datetime.strptime(request.GET['date'], '%d/%m/%Y')
  except:
    m.date_reservation = datetime.datetime.today()
    m.date_filled = False

  m.save()

  try:
    m.message_sent = m.send()
  except Exception as e:
    m.message_sent = False

    import logging
    log = logging.getLogger('django.request')
    log.exception("Couldn't send e-mail (message #%s)" % m.id)

  m.save()

  json_data = dict()
  json_data['result'] = \
    u'Merci de votre message %s, vous recevrez notre réponse dans les plus brefs délais' % unicode(m.firstname)
  json_data = json.dumps(json_data)

  response = HttpResponse(json_data, content_type='application/json')
  response['Content-Length'] = len(json_data)

  return response
