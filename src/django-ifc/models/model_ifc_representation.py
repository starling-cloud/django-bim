# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Representation Model Class
=======================================


For detailed specifications, see:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcrepresentationresource/lexical/ifcrepresentation.htm

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

__all__ = ["IfcRepresentation", ]


# =============================================================================
# Classes
# =============================================================================

class IfcRepresentation(models.Model):
    """
    """

class IfcRepresentation(models.Model):
    """
    Model representing an IfcRepresentation as defined in the IFC 2x3 standard.

    This model defines the representation of a product in a specific representation context, 
    such as the geometry or spatial structure.

    Attributes:
        context_of_items (ForeignKey): The context in which the items are represented.
        representation_identifier (CharField): Identifier of the representation, e.g., 'Body', 'Axis'.
        representation_type (CharField): The type of the representation, e.g., 'Mesh', 'Solid'.
        items (ManyToManyField): Items that are part of this representation.
    """

    context_of_items = models.ForeignKey(
        IfcRepresentationContext,
        on_delete=models.CASCADE,
        verbose_name=_("Context of Items"),
        help_text=_("The context that defines how the representation items are interpreted.")
    )

    representation_identifier = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Representation Identifier"),
        help_text=_("Identifier of the representation, such as 'Body' for geometric representation or 'Axis' for symbolic representation.")
    )
    representation_type = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Representation Type"),
        help_text=_("The type of the representation, such as 'Mesh', 'Solid', or 'Curve'.")
    )
    items = models.ManyToManyField(
        IfcRepresentationItem,
        verbose_name=_("Items"),
        help_text=_("Geometric or spatial items included in this representation.")
    )

    class Meta:
        verbose_name = _("IfcRepresentation")
        verbose_name_plural = _("IfcRepresentations")

    def __str__(self):
        return f"{self.representation_identifier} - {self.representation_type}"
