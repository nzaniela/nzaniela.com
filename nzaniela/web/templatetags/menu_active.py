import re

from django import template
from django.core.urlresolvers import reverse, NoReverseMatch

from nzaniela.web.snippets import Footer


register = template.Library()


@register.simple_tag(takes_context=True)
def menu_active(context, pattern_or_urlname):
    try:
        # handle slash
        if reverse(pattern_or_urlname) == '/':
            pattern = '^/$'
        else:
            pattern = '^' + reverse(pattern_or_urlname) + "([-\w]+)?"
    except NoReverseMatch:
        pattern = pattern_or_urlname

    if context.get('request'):
        path = context.get('request').path

        if re.search(pattern, path):
            return 'selected'
        return ''


@register.inclusion_tag('tags/footer.html', takes_context=True)
def footer(context):
    return {
        'footer': Footer.objects.first(),
        'request': context.get('request'),
    }
