from django.db import models
from home.blocks import DocumentLinkWithChildrenBlock
from home.blocks import ExternalLinkWithChildrenBlock
from home.blocks import InternalLinkWithChildrenBlock
from home.blocks import NewsBlock
from home.blocks import PartnersBlock
from home.blocks import ServicesBlock
from home.blocks import SlidersBlock
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import MultiFieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.snippets.models import register_snippet


"""
Snippets
"""


@register_snippet
class Navbar(models.Model):
    name = models.CharField(max_length=100, verbose_name="Menu Name")
    items = StreamField(
        [
            ("external", ExternalLinkWithChildrenBlock()),
            ("internal", InternalLinkWithChildrenBlock()),
            ("document", DocumentLinkWithChildrenBlock()),
        ],
    )

    panels = [FieldPanel("name"), FieldPanel("items")]

    def __str__(self):
        return self.name


"""
Pages
"""


class HomePage(Page):
    # properties
    max_count = 1

    sections = StreamField(
        [
            ("slider", SlidersBlock()),
            ("services", ServicesBlock()),
            ("news", NewsBlock()),
            ("partners", PartnersBlock()),
        ],
    )

    content_panels = [*Page.content_panels, FieldPanel("sections")]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ]
