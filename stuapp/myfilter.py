import markdown
from django.template import Library

register = Library()
"""s"""
@register.filter
def md(value):
    return markdown.markdown(value)