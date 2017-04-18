from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

class AboutPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

class ProjectsPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

class ProjectsSubPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    @property
    def projectList(self):
        # Get list of live blog pages that are descendants of this page
        project_list = Project.objects.live().descendant_of(self)

        return project_list

class Project(Page):
    project_subtitle = models.CharField(max_length=255)
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('project_subtitle', classname="full"),
    ]

class ContactPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]