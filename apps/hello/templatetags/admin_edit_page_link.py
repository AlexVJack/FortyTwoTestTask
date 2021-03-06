from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def edit_link(object):
    return reverse('admin:%s_%s_change' % (
        object._meta.app_label,
        object._meta.model_name),
        args=(object.id,))
