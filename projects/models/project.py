from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField
from django.utils.translation import ugettext_lazy as _

from .attribute import Attribute


class ProjectType(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))

    class Meta:
        verbose_name = _('project type')
        verbose_name_plural = _('project types')
        ordering = ('name',)

    def __str__(self):
        return self.name


class Project(models.Model):
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(verbose_name=_('modified at'), auto_now=True, editable=False)
    name = models.CharField(max_length=255, verbose_name=_('name'))
    identifier = models.CharField(max_length=50, verbose_name=_('identifier'), db_index=True, blank=True, null=True)
    type = models.ForeignKey(ProjectType, verbose_name=_('type'), related_name='projects', on_delete=models.PROTECT)
    attribute_data = JSONField(verbose_name=_('attribute data'), default=dict, blank=True, null=True)
    phase = models.ForeignKey('ProjectPhase', verbose_name=_('phase'), null=True, related_name='projects',
                              on_delete=models.PROTECT)

    geometry = models.MultiPolygonField(null=True, blank=True)

    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')
        ordering = ('id',)

    def __str__(self):
        return self.name


class ProjectPhase(models.Model):
    project_type = models.ForeignKey(ProjectType, verbose_name=_('project type'), on_delete=models.CASCADE,
                                     related_name='phases')
    name = models.CharField(max_length=255, verbose_name=_('name'))
    color = models.CharField(max_length=64, verbose_name=_('color'), blank=True)
    index = models.PositiveIntegerField(verbose_name=_('index'), default=0)

    class Meta:
        verbose_name = _('project phase')
        verbose_name_plural = _('project phases')
        unique_together = ('project_type', 'index')
        ordering = ('project_type', 'index',)

    def __str__(self):
        return self.name


class ProjectPhaseSection(models.Model):
    phase = models.ForeignKey(ProjectPhase, verbose_name=_('phase'), related_name='sections', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name=_('name'))
    index = models.PositiveIntegerField(verbose_name=_('index'), default=0)
    attributes = models.ManyToManyField(
        Attribute, verbose_name=_('attributes'), related_name='phase_sections', through='ProjectPhaseSectionAttribute'
    )

    class Meta:
        verbose_name = _('project phase section')
        verbose_name_plural = _('project phase sections')
        unique_together = ('phase', 'index')
        ordering = ('phase', 'index')

    def __str__(self):
        return self.name

    def get_attribute_identifiers(self):
        return [a.identifier for a in self.attributes.all()]


class ProjectPhaseSectionAttribute(models.Model):
    attribute = models.ForeignKey(Attribute, verbose_name=_('attribute'), on_delete=models.CASCADE)
    section = models.ForeignKey(ProjectPhaseSection, verbose_name=_('phase section'), on_delete=models.CASCADE)
    generated = models.BooleanField(verbose_name=_('generated'), default=False)
    required = models.BooleanField(verbose_name=_('required'))
    index = models.PositiveIntegerField(verbose_name=_('index'), default=0)

    class Meta:
        verbose_name = _('project phase section attribute')
        verbose_name_plural = _('project phase section attributes')
        unique_together = ('section', 'index')
        ordering = ('section', 'index')

    def __str__(self):
        return '{} {} {} {}'.format(self.attribute, self.section, self.section.phase, self.index)
