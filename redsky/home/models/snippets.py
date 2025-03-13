from django.db import models
from home.blocks import DocumentLinkWithChildrenBlock
from home.blocks import ExternalLinkWithChildrenBlock
from home.blocks import InternalLinkWithChildrenBlock
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import TranslatableMixin
from wagtail.snippets.models import register_snippet


@register_snippet
class Navbar(TranslatableMixin, models.Model):
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
