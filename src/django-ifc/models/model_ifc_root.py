# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Root Model Class
=============================

This module defines an abstract base class for all IFC models, ensuring
consistency and reusability across different IFC entities within the
Django application.

Definition from buildingSMART:
The IfcRoot is the most abstract and root class for all IFC entity definitions
that roots in the kernel or in subsequent layers of the IFC object model.
It is therefore the common supertype all all IFC entities, beside those
defined in an IFC resource schema. All entities that are subtypes of IfcRoot
can be used independently, whereas resource schema entities, that are not
subtypes of IfcRoot, are not supposed to be independent entities.

https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifckernel/lexical/ifcroot.htm

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
# from uuid import uuid4
# from typing import Any, Dict, List

# Import | Libraries
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Import | Local Modules
from ..fields.model import (
    IfcGloballyUniqueIdField,
    IfcLabelField,
    IfcTextField,
)


# =============================================================================
# Variables
# =============================================================================

__all__ = ["IfcRootModel", ]


# =============================================================================
# Classes
# =============================================================================

class IfcRootModel(models.Model):
    """
    IFC Root Model Class
    ====================

    This abstract base class provides common fields and functionality for all
    IFC models, such as a unique global identifier and metadata regarding
    the creation and modification history of the entity.

    Attributes:
        global_id (IfcGloballyUniqueIdField): A unique identifier for the
            entity within the IFC model.
        name (IfcLabelField): The name of the IFC entity.
        description (IfcTextField): A description of the IFC entity.
        owner_history (ForeignKey): A link to the ownership history of the
            entity.

    Note:
        This class is not meant to be instantiated directly.

    """

    global_id = IfcGloballyUniqueIdField(
        help_text=_("Globally unique identifier in the IFC model.")
    )

    name = IfcLabelField(
        blank=True,
        null=True,
        verbose_name=_("name"),
        help_text=_("Name of the IFC entity.")
    )

    description = IfcTextField(
        blank=True,
        null=True,
        verbose_name=_("description"),
        help_text=_("Description of the IFC entity.")
    )

    owner_history = models.ForeignKey(
        'IfcOwnerHistory',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='owned_entities',
        verbose_name=_("owner history"),
        help_text=_("Ownership history of the object.")
    )

    class Meta:
        abstract = True
        verbose_name = _("IFC Root Model")
        verbose_name_plural = _("IFC Root Models")

    def __str__(self):
        return self.name or _("Unnamed IFC Entity")

    def get_absolute_url(self):
        return reverse('ifc_entity_detail', kwargs={'pk': self.pk})
