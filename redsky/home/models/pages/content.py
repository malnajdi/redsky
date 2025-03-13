from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import InlinePanel
from wagtail.admin.panels import PageChooserPanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable
from wagtail.models import Page


class PostRelatedPosts(Orderable):
    page = ParentalKey(
        "PostPage",
        on_delete=models.CASCADE,
        related_name="related_posts",
    )

    related_post = models.ForeignKey(
        "home.PostPage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        PageChooserPanel("related_post", "home.PostPage"),
    ]


class PostIndexPage(Page):
    # properties
    max_count = 1
    parent_page_types = ["home.HomePage"]
    subpage_types = ["home.PostPage"]
    template = "home/pages/posts.html"

    description = models.CharField("Description", max_length=255, blank=True)

    content_panels = [*Page.content_panels, FieldPanel("description")]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = PostPage.objects.child_of(self).live()
        return context


class PostPage(Page):
    # properties
    parent_page_types = ["home.PostIndexPage"]
    template = "home/pages/post.html"

    description = models.CharField("Description", max_length=255, blank=True)

    content = RichTextField()

    content_panels = [
        *Page.content_panels,
        FieldPanel("description"),
        FieldPanel("content"),
        InlinePanel("related_posts"),
    ]
