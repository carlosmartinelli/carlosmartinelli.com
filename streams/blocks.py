# # from wagtail.core import blocks
# from wagtail import blocks

# # from wagtail.core.templatetags.wagtailcore_tags import richtext


# class TitleAndTextBlock(blocks.StructBlock):
#     """Title and text and nothing else."""

#     title = blocks.CharBlock(required=True, help_text="Add your title")
#     text = blocks.TextBlock(required=True, help_text="Add additional text")

#     class Meta:  # noqa
#         template = "title_and_text_block.html"
#         icon = "edit"
#         label = "Title & Text"

from wagtail import blocks


class ImageText(blocks.StructBlock):
    reverse = BooleanBlock(required=False)
    text = RichTextBlock()
    image = CustomImageChooserBlock()


class BodyBlock(StreamBlock):
    h1 = CharBlock()
    h2 = CharBlock()
    paragraph = RichTextBlock()

    image_text = ImageText()
    image_carousel = ListBlock(ImageChooserBlock())
    thumbnail_gallery = ListBlock(ImageChooserBlock())