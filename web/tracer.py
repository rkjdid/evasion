import threading
import models
from urlparse import urlparse

lock = threading.Lock()

def trace_user(request):
  with lock:
    ref = request.META.get('HTTP_REFERER')

    if ref:
      ref = urlparse(request.META.get('HTTP_REFERER'))
      r, _ = models.Referer.objects.get_or_create(
        host=ref.netloc
      )
    else:
      r, _ = models.Referer.objects.get_or_create(host="none")

    r.hits += 1
    r.save()

    v, _ = models.Visitor.objects.get_or_create(
      ip=get_ip(request)
    )
    v.hits += 1
    v.save()

    rv, _ = models.VisitorReferer.objects.get_or_create(
      visitor=v, referer=r
    )
    rv.count += 1
    rv.save()

    return v

def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
