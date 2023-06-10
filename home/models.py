from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.fields import StreamField
# from wagtail.admin.panels import FieldPanel, StreamFieldPanel
# from wagtail.images.blocks import ImageChooserBlock
# from streams import blocks.BodyBlock


from streams import blocks



class HomePage(Page):
    template = "home/index.html"

    body = StreamField(BodyBlock(), blank=True)


    # body = RichTextField(blank=True)

    # body = StreamField([
    #     ('heading', blocks.CharBlock(form_classname="title")),
    #     ('paragraph', blocks.RichTextBlock()),
    #     ('image', ImageChooserBlock()),
    # ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        StreamFieldPanel('content'),
    ]
