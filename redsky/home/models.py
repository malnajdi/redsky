from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import MultiFieldPanel
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageBlock
from wagtail.models import Page


class HomePage(Page):
    hero_section = StreamField(
        [
            ("image", ImageBlock()),
        ],
        block_counts={
            "heading": {"min_num": 1},
            "image": {"max_num": 5},
        },
    )

    body = StreamField(
        [
            ("heading", blocks.CharBlock(form_classname="title")),
            ("paragraph", blocks.RichTextBlock()),
            ("image", ImageBlock()),
        ],
        block_counts={
            "heading": {"min_num": 1},
            "image": {"max_num": 5},
        },
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        # FieldPanel("hero_section"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ]
