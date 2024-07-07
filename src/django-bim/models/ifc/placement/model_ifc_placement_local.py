# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Local Placement Model Class
========================================

This module defines the IfcLocalPlacementModel class, representing an
IfcLocalPlacement entity as specified in the IFC standard. This model is
used to define the placement of objects relative to the placement of other
objects, allowing hierarchical structuring of spatial object placement
within a project.

More information on IfcLocalPlacement can be found here:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcgeometricconstraintresource/lexical/ifclocalplacement.htm

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library

# Import | Libraries
from django.db import models
from django.utils.translation import gettext_lazy as _

# Import | Local Modules
from .model_ifc_placement_object import IfcObjectPlacementModel


# =============================================================================
# Classes
# =============================================================================

class IfcLocalPlacementModel(IfcObjectPlacementModel):
    """
    IFC Local Placement Model Class
    ===============================

    Model representing an IfcLocalPlacement, which defines an object placement
    relative to the placement of another object.

    Extends the IfcObjectPlacementModel to provide specific functionalities for
    local placements, allowing objects to be positioned relative to one
    another.

    Attributes:
        relative_placement (ForeignKey): References another instance of
            IfcLocalPlacementModel to which this object's placement is
            relative. This allows constructing a hierarchy of object
            placements.

    """

    # Class | Model Fields
    # =========================================================================

    relative_placement = models.ForeignKey(
        "self",
        on_delete = models.CASCADE,
        null = True,
        blank = True,
        related_name = "related_placements",
        verbose_name = _("Relative Placement"),
        help_text = _(
            "References another placement to which this placement is relative."  # noqa E501
        ),
    )

    # Class | Model Methods
    # =========================================================================

    def __str__(self) -> str:
        """
        String representation of the IfcLocalPlacementModel, showing its
        unique ID and any relative placement.
        """
        relative_info = f"relative to: {self.relative_placement.placement_id}" if self.relative_placement else "with no relative placement"  # noqa E501
        return f"Local Placement ID {self.id} ({relative_info})"


# =============================================================================
# Module Variables
# =============================================================================

__all__ = [
    "IfcLocalPlacementModel",
]
