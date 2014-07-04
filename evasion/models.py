from django.db import models

import datetime, pytz
import settings

import mail


class Message (models.Model):
  class Meta:
    ordering = ['-id']

  email = models.CharField(
    'Mail',
    max_length=60, null=False, blank=False, default="")
  firstname = models.CharField(
    'First Name',
    max_length=60, null=False, blank=False)

  lastname = models.CharField(
    'Name',
    max_length=60, null=True, blank=True)

  phone = models.CharField(
    'Phone',
    max_length=20, null=True, blank=True)

  date_reservation = models.DateField(
    'Reservation Date')

  date_filled = models.BooleanField(
    'Reservation Date filled',
    default=False)

  message = models.TextField(
    'Message',
    null=True, blank=True)

  message_sent = models.BooleanField(
    'Message sent',
    default=False)

  date_message = models.DateTimeField(
    'Message Date',
    default=datetime.datetime.now(tz=pytz.timezone(settings.TIME_ZONE)))

  def send(self):
    return mail.sendMail(
      self.pk, self.email, self.firstname,
      self.lastname, self.phone, self.date_filled,
      self.date_reservation, self.date_message, self.message)

  def __unicode__(self):
    return "#%s/%s/%s" % (self.id, self.firstname, self.email)
