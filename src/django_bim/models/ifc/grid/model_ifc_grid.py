# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Grid Model Class
=============================

This module defines the Django model for the IfcGrid entity as specified in the
IFC 2x3 standard, which is used to organize spatial elements and provide
reference points within a project's design and construction stages.

Grid systems are crucial in layout planning and are typically composed of two
or three sets of parallel lines that intersect at defined points. This model
supports both 2D and 3D grid systems by allowing an optional set of W axes.

More information on IfcGrid can be found here:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcproductextension/lexical/ifcgrid.htm

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library

# Import | Libraries
from django.db import models
from django.utils.translation import gettext_lazy as _

# Import | Grid Modules
from ..model_ifc_product import IfcProductModel
from .model_ifc_grid_axis import IfcGridAxisModel


# =============================================================================
# Classes
# =============================================================================

class IfcGridModel(IfcProductModel):
    """
    IFC Grid Model Class
    ====================

    Django model representing an IfcGrid as defined in the IFC 2x3 standard.

    An IfcGrid is used to define a grid system within a project, typically
    used for aligning elements during the design and construction phases.

    Attributes:
        u_axes (ManyToManyField): The set of U axes in the grid.
        v_axes (ManyToManyField): The set of V axes in the grid.
        w_axes (ManyToManyField): The set of W axes in the grid,
            optional for 3D grids.

    """

    # Class | Model Fields
    # =========================================================================

    u_axes = models.ManyToManyField(
        IfcGridAxisModel,
        related_name='u_axes',
        verbose_name=_("U Axes"),
        help_text=_("The U axes of the grid."),
    )

    v_axes = models.ManyToManyField(
        IfcGridAxisModel,
        related_name='v_axes',
        verbose_name=_("V Axes"),
        help_text=_("The V axes of the grid."),
    )

    w_axes = models.ManyToManyField(
        IfcGridAxisModel,
        blank=True,
        related_name='w_axes',
        verbose_name=_("W Axes"),
        help_text=_("The W axes of the grid, optional for 3D grids."),
    )

    # Class | Model Meta Class
    # =========================================================================

    class Meta:
        """
        Meta Class
        ----------

        """
        verbose_name = _("IFC Grid")
        verbose_name_plural = _("IFC Grids")

    # Class | Model Methods
    # =========================================================================

    def __str__(self) -> str:
        """
        Provides a string representation of the grid, typically for
        admin displays.
        """
        grid_dimensions = "3D" if self.w_axes.exists() else "2D"
        return f"{self.name} - {grid_dimensions} Grid"


# =============================================================================
# Module Variables
# =============================================================================

__all__ = [
    "IfcGridModel",
]
