from wagtail import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class SliderBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    media = blocks.StreamBlock(
        [
            ("image", ImageChooserBlock()),
            ("video", EmbedBlock()),
        ],
    )


class ServiceBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    description = blocks.CharBlock()
    image = ImageChooserBlock()


class SlidersBlock(blocks.StructBlock):
    slides = blocks.StreamBlock(
        [
            ("slide", SliderBlock()),
        ],
    )

    class Meta:
        template = "home/blocks/slides.html"


class ServicesBlock(blocks.StructBlock):
    services = blocks.StreamBlock(
        [
            ("service", ServiceBlock()),
        ],
    )

    class Meta:
        template = "home/blocks/services.html"


class NewsBlock(blocks.StructBlock):
    news = blocks.StreamBlock(
        [
            ("post", blocks.PageChooserBlock()),
        ],
    )

    class Meta:
        template = "home/blocks/news.html"


class PartnersBlock(blocks.StructBlock):
    partners = blocks.StreamBlock(
        [
            ("partner", ImageChooserBlock()),
        ],
    )

    class Meta:
        template = "home/blocks/partners.html"
