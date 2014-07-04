# -*- coding: utf-8 -*-
import smtplib, re

from email.mime.text import MIMEText

import settings

def sendMail(pk, email, firstname, lastname, phone, date_filled, date_reservation, date_message, message):
  text =\
    u"E-mail: %s\n" % unicode(email) + \
    u"Prénom: %s\n" % unicode(firstname) + \
    u"Nom: %s\n" % unicode(lastname) + \
    u"Téléphone: %s\n" % unicode(phone)

  if date_filled:
    text += u"Date de réservation: %s\n" % date_reservation
  else:
    text += u"Date de réservation non renseignée\n"

  text +=\
    u"Date d'envoi de la réservation: %s\n" % date_message + \
    u"Message: %s" % unicode(message)

  msg = MIMEText(text, "plain", "utf-8")
  msg["Subject"] = u"[Evasion-Antillaise - Réservation#%s]" % pk
  msg["From"] = email
  msg["To"] = settings.MAIL['DEST']

  # Send e-mail
  server = None
  try:
    server = smtplib.SMTP_SSL(settings.MAIL['SERVER'])
    server.login(settings.MAIL['LOGIN'], settings.MAIL['PASS'])

    server.sendmail(email, settings.MAIL['DEST'], msg.as_string().encode('utf-8'))
  except:
    print("Failed to send e-mail (message #%s)" % pk)
    try:
      server.quit()
    finally:
      return False

  print("Mail sent to %s (message #%s)" % (settings.MAIL['DEST'], pk))
  server.quit()
  return True
