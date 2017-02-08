# -*- coding: utf-8 -*-
import smtplib, re

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from evasion import settings

def sendMail(pk, email, firstname, lastname, phone, date_filled, date_reservation, date_message, message):
  text =\
    u"E-mail: %s\n" % email + \
    u"Prénom: %s\n" % firstname + \
    u"Nom: %s\n" % lastname + \
    u"Téléphone: %s\n" % phone

  if date_filled:
    text += u"Date de réservation: %s\n" % date_reservation
  else:
    text += u"Date de réservation non renseignée\n"

  text +=\
    u"Date d'envoi du message: %s\n" % date_message + \
    u"Message: %s" % message

  msg = MIMEMultipart("alternative")
  msg["Subject"] = u"[Evasion-Antillaise - Réservation#%s]" % pk
  msg["To"] = settings.MAIL['DEST']
  msg["From"] = settings.MAIL['FROM']
  msg["Reply-To"] = email.encode("ascii")

  msg_text = MIMEText(text.encode("utf-8"), "plain", "utf-8")

  msg.attach(msg_text)
  msg = msg.as_string()
  #msg = msg.encode("utf-8")

  # Send e-mail
  server = smtplib.SMTP_SSL(settings.MAIL['SERVER'], settings.MAIL['PORT'])
  server.login(settings.MAIL['LOGIN'], settings.MAIL['PASS'])

  server.sendmail(settings.MAIL['FROM'], settings.MAIL['DEST'], msg)
  server.sendmail(settings.MAIL['FROM'], settings.MAIL['ADMIN'], msg)
  server.sendmail(settings.MAIL['FROM'], 'silvynathalie@yahoo.fr', msg)
  server.quit()

  # todo log shit..

  return True

