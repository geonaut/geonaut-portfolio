from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

class AboutPage(Page):
    body_professional = RichTextField(blank=True)
    body_personal = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body_professional', classname="full"),
        FieldPanel('body_personal', classname="full"),
    ]

class ProjectsPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    def get_context(self, request):
        context = super(ProjectsPage, self).get_context(request)
        context['sub_pages'] = self.get_children().specific().live()
        print(context['sub_pages'])
        return context

class IndexPage(Page):
    body = RichTextField(blank=True)
    button_text = models.CharField(max_length=255,null=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('button_text', classname="full"),
        ImageChooserPanel('feed_image'),
    ]

    def get_context(self, request):
        context = super(IndexPage, self).get_context(request)
        context['sub_pages'] = self.get_children().specific().live()
        print(context['sub_pages'])
        return context

class GridSubPage(Page):
    body = RichTextField(blank=True)
    button_text = models.CharField(max_length=255,null=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('button_text', classname="full"),
        ImageChooserPanel('feed_image'),
    ]

    def get_context(self, request):
        context = super(GridSubPage, self).get_context(request)
        context['sub_pages'] = self.get_children().specific().live()
        print(context['sub_pages'])
        return context

class ListSubPage(Page):
    body = RichTextField(blank=True)
    button_text = models.CharField(max_length=255,null=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('button_text', classname="full"),
        ImageChooserPanel('feed_image'),
    ]

    def get_context(self, request):
        context = super(ListSubPage, self).get_context(request)
        context['sub_pages'] = self.get_children().specific().live()
        print(context['sub_pages'])
        return context

class ProjectsSubPage(Page):
    body = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        ImageChooserPanel('feed_image'),
    ]

    @property
    def projectList(self):
        # Get list of live blog pages that are descendants of this page
        project_list = Project.objects.live().descendant_of(self)

        return project_list

class ProjectsSubPage(Page):
    body = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        ImageChooserPanel('feed_image'),
    ]

    @property
    def projectList(self):
        # Get list of live blog pages that are descendants of this page
        project_list = Project.objects.live().descendant_of(self)

        return project_list

class Project(Page):
    project_subtitle = models.CharField(max_length=255)
    body = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    link_external = models.URLField(blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        else:
            return self.link_external
    
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('project_subtitle', classname="full"),
        ImageChooserPanel('feed_image'),
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
    ]

class ContactPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

class LinksPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    @property
    def linkURL(self):
        return self.link_external

    @property
    def linkList(self):
        # Get list of live blog pages that are descendants of this page
        link_list = Link.objects.live().descendant_of(self)

        return link_list

class Link(Page):
    link_subtitle = models.CharField(max_length=255)
    body = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    link_external = models.URLField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('link_subtitle', classname="full"),
        ImageChooserPanel('feed_image'),
        FieldPanel('link_external'),
    ]

class Item(Page):
    item_subtitle = models.CharField(max_length=255,blank=True)
    body = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    link_external = models.URLField(blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        else:
            return self.link_external
    
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('item_subtitle', classname="full"),
        ImageChooserPanel('feed_image'),
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
    ]