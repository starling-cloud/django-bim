from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _

class IfcUnitRelation(models.Model):
    """
    Model to facilitate a GenericRelation from IfcUnitAssignment to various IfcUnit models
    """
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    unit = GenericRelation('IfcUnit', related_query_name='unit_relations')

    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"{self.content_object}"
