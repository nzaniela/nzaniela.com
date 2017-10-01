from __future__ import unicode_literals

from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, PageChooserPanel
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet


class LinkFields(models.Model):
    """
    Link to an external  page , document  or the
    same  page
    """
    link_external = models.URLField(
        "External link",
        blank=True,
        null=True,
        help_text='Set  an external link if  you want the link to  link  outside the cms'
    )
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        related_name='+',
        help_text='Choose  an existing page  if you want to  point  inside  the cms'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        related_name='+',
        help_text='Choose  and  existing document if  you want the link to  open a document',
    )
    link_email = models.EmailField(
        blank=True,
        null=True,
        help_text='Set the  recipient  email address if you want  link to  send email'
    )
    link_phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text='Set the number if you want  the  link to dial a  phone  number'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_external:
            return self.link_external
        elif self.link_document:
            return self.link_document.url
        elif self.link_email:
            return 'mailto:%s' % self.link_email
        elif self.link_phone:
            return 'tel:%s' % self.link_phone.strip()
        else:
            return "#"

    panel = [
        MultiFieldPanel([
            PageChooserPanel('link_page'),
            FieldPanel('link_external'),
            DocumentChooserPanel('link_document'),
            FieldPanel('link_email'),
            FieldPanel('link_phone'),
        ],
            "Link"
        ),
    ]

    class Meta:
        abstract = True


@register_snippet
class Teammate(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField()
    initial_photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    secondary_photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('initial_photo'),
        ImageChooserPanel('secondary_photo'),
        FieldPanel('description')
    ]

    def __str__(self):
        return self.name


@register_snippet
class Technology(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    description = RichTextField()

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('logo'),
        FieldPanel('description')
    ]

    def __str__(self):
        return self.name


@register_snippet
class Client(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField()
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('logo'),
        FieldPanel('description'),
    ]

    def __str__(self):
        return self.name


@register_snippet
class Project(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, null=True, blank=True)

    description = RichTextField()

    demo_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    technologies = models.ManyToManyField(Technology)
    panels = [
        FieldPanel('name'),
        ImageChooserPanel('demo_image'),
        FieldPanel('description'),
        FieldPanel('client'),
        FieldPanel('technologies'),
    ]

    def __str__(self):
        return self.name


@register_snippet
class Footer(models.Model):
    links_text = models.CharField(max_length=255)
    contact_text = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    popup_text = RichTextField()
    popup_heading = models.CharField(max_length=255)

    links = StreamField([
        ('link', blocks.StructBlock([
            ('text', blocks.TextBlock()),
            ('url', blocks.URLBlock()),
        ], template='streams/footer_link.html'))
    ])

    panels = [
        FieldPanel('links_text'),
        FieldPanel('contact_text'),
        FieldPanel('button_text'),
        FieldPanel('popup_text'),
        FieldPanel('popup_heading'),
        StreamFieldPanel('links'),
    ]

    def __str__(self):
        return self.links_text


@register_snippet
class Category(models.Model):
    name = models.CharField(max_length=55)

    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name
