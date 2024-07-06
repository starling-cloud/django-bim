# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Base Model Class
=============================

This module defines an abstract base class for all IFC models, ensuring
consistency and reusability across different IFC entities within the
Django application.

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
from uuid import uuid4
# from typing import Any, Dict, List

# Import | Libraries
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Import | Local Modules


# =============================================================================
# Variables
# =============================================================================

__all__ = ["IfcBaseModel", ]


# =============================================================================
# Classes
# =============================================================================

class IfcBaseModel(models.Model):
    """
    IFC Base Model Class
    ====================

    This abstract base class provides common fields and functionality for all
    IFC models, such as a unique global identifier and metadata regarding
    the creation and modification history of the entity.

    Attributes:
        global_id (UUIDField): A unique identifier for the entity within the
            IFC model.
        name (CharField): The name of the IFC entity.
        description (TextField): A description of the IFC entity.
        owner_history (ForeignKey): A link to the ownership history of the
            entity.

    Note:
        This class is not meant to be instantiated directly.

    """

    global_id = models.UUIDField(
        default=uuid4,
        unique=True,
        editable=False,
        help_text=_("Globally unique identifier in the IFC model.")
    )

    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("name"),
        help_text=_("Name of the IFC entity.")
    )

    description = models.TextField(
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
        verbose_name = _("IFC Base Model")
        verbose_name_plural = _("IFC Base Models")

    def __str__(self):
        return self.name or _("Unnamed IFC Entity")

    def get_absolute_url(self):
        return reverse('ifc_entity_detail', kwargs={'pk': self.pk})
