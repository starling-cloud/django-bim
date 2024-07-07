# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Grid Placement Model Class
=======================================



More information on IfcGridPlacement can be found here:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcgeometricconstraintresource/lexical/ifcgridplacement.htm

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library

# Import | Libraries
from django.db import models
from django.utils.translation import gettext_lazy as _

# Import | Grid Modules
from .model_ifc_placement_object import IfcObjectPlacementModel
from .model_ifc_grid import IfcGridModel


# =============================================================================
# Classes
# =============================================================================

class IfcGridPlacementModel(IfcObjectPlacementModel):
    """
    IFC Grid Placement Model Class
    ==============================

    Model representing an IfcGridPlacement as defined in the IFC standard.

    This model specifies the placement of objects within a project by referring
    to a grid structure.

    Attributes:
        grid (ForeignKey): The grid used for this placement.
        placement_location (CharField): Descriptive location within the grid,
            e.g., intersection name or axis identifier.
    """

    # Class | Model Fields
    # =========================================================================

    # grid = models.ForeignKey(
    #     IfcGridModel,
    #     on_delete = models.CASCADE,
    #     verbose_name = _("Grid"),
    #     help_text = _("The grid used for this placement.")
    # )

    placement_location = models.CharField(
        max_length = 255,
        verbose_name = _("Placement Location"),
        help_text = _(
            "Descriptive location within the grid, such as 'A1', 'B2', etc."
        ),
    )

    # Class | Model Methods
    # =========================================================================

    def __str__(self) -> str:
        """
        """
        return f"{self.grid.name} at {self.placement_location}"


# =============================================================================
# Module Variables
# =============================================================================

__all__ = [
    "IfcGridPlacementModel",
]
