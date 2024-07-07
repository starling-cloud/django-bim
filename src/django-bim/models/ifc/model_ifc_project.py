# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Project Model Class
================================


For detailed specifications, see:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifckernel/lexical/ifcproject.htm

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
from ...fields.model import (
    IfcLabelField,
)
from .ifc_unit_assignment import IfcUnitAssignment  # Assume this handles the units used throughout the project
from .ifc_geometric_representation_context import IfcGeometricRepresentationContext  # Assume this handles the geometric context


# =============================================================================
# Variables
# =============================================================================


# =============================================================================
# Classes
# =============================================================================

class IfcProjectModel(IfcObjectDefinitionModel):
    """
    IFC Project Model Class
    =======================

    Model representing an IfcProject as defined in the IFC 2x3 standard.

    This model encapsulates the top-level project information in an IFC file,
    providing a context for all project-related data, including project name, geographic
    and geometric context, and units of measurement.

    Attributes:
        long_name (models.CharField): A long and more descriptive name for the project.
        phase (models.CharField): The current phase of the project (e.g., design, construction).
        units_in_context (ForeignKey): The units used in this project.
        representation_contexts (ManyToManyField): Contexts that define the geometric representation.
    """

    # Class | Model Fields
    # =========================================================================

    long_name = IfcLabelField(
        blank=True,
        null=True,
        verbose_name=_("Long Name"),
        help_text=_("A longer and more descriptive name for the project.")
    )

    phase = IfcLabelField(
        blank=True,
        null=True,
        verbose_name=_("Phase"),
        help_text=_("The current phase of the project such as planning, construction, or operation.")  # noqa E501
    )

    units_in_context = models.ForeignKey(
        IfcUnitAssignment,
        on_delete=models.RESTRICT,
        verbose_name=_("Units In Context"),
        help_text=_("The units used within this project.")
    )

    representation_contexts = models.ManyToManyField(
        IfcGeometricRepresentationContext,
        verbose_name=_("Geometric Representation Contexts"),
        help_text=_("Geometric contexts that define how the geometries are represented in the project.")
    )

    # Class | Model Meta Class
    # =========================================================================

    class Meta:
        """
        Meta Class
        ----------

        """
        verbose_name = _("IFC Project")
        verbose_name_plural = _("IFC Projects")

    # Class | Model Methods
    # =========================================================================

    def __str__(self) -> str:
        """
        """
        return f"{self.long_name} - Phase: {self.phase}"


# =============================================================================
# Module Variables
# =============================================================================

__all__ = [
    "IfcProjectModel",
]
