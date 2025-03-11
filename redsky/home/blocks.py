from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock


class ServiceBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    description = blocks.CharBlock()
    image = ImageChooserBlock()


class SlidersBlock(blocks.StructBlock):
    slides = blocks.StreamBlock(
        [
            ("image", ImageChooserBlock(required=False)),
            ("video", blocks.URLBlock(required=False)),
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


"""
URL BLOCKS
"""


class BaseLinkBlock(blocks.StructBlock):
    title = blocks.CharBlock()


class ExternalLinkBlock(BaseLinkBlock):
    link = blocks.URLBlock(required=True)

    class Meta:
        template = "home/blocks/links/external.html"


class InternalLinkBlock(BaseLinkBlock):
    link = blocks.PageChooserBlock(required=True)

    class Meta:
        template = "home/blocks/links/internal.html"


class DocumentLinkBlock(BaseLinkBlock):
    link = DocumentChooserBlock(required=True)

    class Meta:
        template = "home/blocks/links/document.html"


class ChildrenLinkBlock(blocks.StructBlock):
    children = blocks.StreamBlock(
        [
            ("external", ExternalLinkBlock()),
            ("internal", InternalLinkBlock()),
            ("document", DocumentLinkBlock()),
        ],
        required=False,
    )


class ExternalLinkWithChildrenBlock(ChildrenLinkBlock, ExternalLinkBlock):
    pass


class InternalLinkWithChildrenBlock(ChildrenLinkBlock, InternalLinkBlock):
    pass


class DocumentLinkWithChildrenBlock(ChildrenLinkBlock, DocumentLinkBlock):
    pass
