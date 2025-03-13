from django import template
from django.utils.translation import get_language
from home.models.snippets import Navbar


register = template.Library()


@register.inclusion_tag("home/templatetags/header.html", takes_context=True)
def navbar_header(context, user=None):
    navbar, created = Navbar.objects.get_or_create(name="Header_EN")
    if get_language() == "ar":
        navbar, created = Navbar.objects.get_or_create(name="Header_AR")
    return {"navbar": navbar}
