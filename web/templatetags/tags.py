from django.template import Library
from django.contrib.staticfiles.templatetags.staticfiles import static

register = Library()

@register.filter
def get_range(to_value):
  """
    Filter - returns a list containing range made from given value
    Usage (in template):

    <ul>{% for i in 3|get_range %}
      <li>{{ i }}. Do something</li>
    {% endfor %}</ul>

    Results with the HTML:
    <ul>
      <li>0. Do something</li>
      <li>1. Do something</li>
      <li>2. Do something</li>
    </ul>

    Instead of 3 one may use the variable set in the views
  """
  return range(to_value)

@register.filter
def get_onerange(to_value):
  return range(1, to_value)

@register.filter
def get_tworange(to_value):
  return range(2, to_value)

@register.simple_tag
def static_fmt(s, i):
  print(s, static(s), i, static(s) % i)
  return static(s % i)

