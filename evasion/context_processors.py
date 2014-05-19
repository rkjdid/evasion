from django.conf import settings

def debug(context):
  print settings.DEBUG
  return {
    'DEBUG': settings.DEBUG
  }