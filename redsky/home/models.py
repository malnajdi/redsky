from home.blocks import NewsBlock
from home.blocks import PartnersBlock
from home.blocks import ServicesBlock
from home.blocks import SlidersBlock
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import MultiFieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page


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
