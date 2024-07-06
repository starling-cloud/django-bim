# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Object Model Class
===============================

This Django model represents an IfcObject as defined in the IFC 2x3 standard,
which serves as a generalization for any entity participating in a project
context. It supports the instantiation of both physical (product) and
non-physical (control elements) entities.

For detailed specifications, see:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifckernel/lexical/ifcobject.htm

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
# from uuid import uuid4
# from typing import Any, Dict, List

# Import | Libraries
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Import | Local Modules
from .model_ifc_object_definition import IfcObjectDefinitionModel
from ..fields.model import (
    IfcLabelField,
)


# =============================================================================
# Variables
# =============================================================================

__all__ = ["IfcObjectModel", ]


# =============================================================================
# Classes
# =============================================================================

class IfcObjectModel(IfcObjectDefinitionModel):
    """
    IFC Object Model Class
    ======================

    Model representing an IfcObject as defined in the IFC 2x3 standard.

    IfcObject is a generalization of any entity that participates in a
    project context and forms the most generic instantiation of all entities
    that are used within IFC. It may represent objects that are physical
    (product) or non-physical (control elements).

    Attributes:
        object_type (models.CharField): A user-defined type for the object that
            can further classify the specific object types beyond the system
            provided by the entity type name.

    """

    object_type = IfcLabelField(
        blank=True,
        null=True,
        verbose_name=_("Object Type"),
        help_text=_("A user-defined type to classify the object beyond its classification by entity type.")  # noqa E501
    )

    class Meta:
        verbose_name = _("IfcObject")
        verbose_name_plural = _("IfcObjects")
        abstract = True  # This model remains abstract and should be inherited

    def __str__(self):
        """
        Provides a human-readable string that is more informative,
        especially in admin or logs.
        """
        return f"{self.name} - {self.object_type}" if self.object_type else super().__str__()  # noqa E501

    def get_absolute_url(self):
        """
        Generate the absolute URL for an object instance to aid in admin
        navigation or UI display.
        """
        return reverse('ifc_object_detail', kwargs={'pk': self.pk})
