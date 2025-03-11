from django import template
from home.models.snippets import Navbar


register = template.Library()


@register.inclusion_tag("home/templatetags/header.html", takes_context=True)
def navbar_header(context, user=None):
    navbar, created = Navbar.objects.get_or_create(name="Header")
    return {"navbar": navbar}
