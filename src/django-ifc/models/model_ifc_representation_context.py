# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Representation Context Model Class
===============================


For detailed specifications, see:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcrepresentationresource/lexical/ifcrepresentationcontext.htm
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

__all__ = ["IfcRepresentationContext", ]


# =============================================================================
# Classes
# =============================================================================

class IfcRepresentationContext(models.Model):
    """
    Model representing an IfcRepresentationContext as defined in the IFC 2x3 standard.

    This model provides a context for all representations, detailing the coordinate system and dimensionality,
    ensuring that the geometric or spatial representations are correctly interpreted according to the project's standards.

    Attributes:
        context_identifier (models.CharField): Identifies the context type (e.g., Plan, Elevation).
        context_type (models.CharField): Describes the context further (e.g., 2D, 3D).
        coordinate_space_dimension (models.IntegerField): The dimensionality of the coordinate system (typically 2 or 3).
    """

    context_identifier = IfcLabelField(
        blank=True,
        null=True,
        verbose_name=_("Context Identifier"),
        help_text=_("Identifies the context type, which could be used to differentiate between different graphical or spatial contexts.")  # noqa E501
    )

    context_type = IfcLabelField(
        blank=True,
        null=True,
        verbose_name=_("Context Type"),
        help_text=_("Further describes the type of representation context, such as 'Model' or 'Plan'.")  # noqa E501
    )

    coordinate_space_dimension = models.IntegerField(
        default=3,
        verbose_name=_("Coordinate Space Dimension"),
        help_text=_("The dimensionality of the coordinate system used in this context, typically 2 or 3.")
    )

    class Meta:
        verbose_name = _("IfcRepresentationContext")
        verbose_name_plural = _("IfcRepresentationContexts")

    def __str__(self):
        return f"{self.context_identifier} ({self.context_type})"

