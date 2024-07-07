# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Grid Axis Model Class
==================================



More information on IfcGrid can be found here:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcgeometricconstraintresource/lexical/ifcgridaxis.htm

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


# =============================================================================
# Classes
# =============================================================================

class IfcGridAxisModel():
    """
    IFC Grid Axis Model Class
    =========================

    Django model representing an IfcGridAxis as defined in the IFC 2x3 standard.

    Represents a single axis within a grid system, which can be labeled and associated with a geometric representation.

    Attributes:
        axis_tag (CharField): The label or identifier for the axis.
        axis_curve (ForeignKey): Optional curve geometry associated with the axis.
        same_sense (BooleanField): Indicates the direction of the grid axis in relation to its geometric representation.
    """


    # Class | Model Fields
    # =========================================================================

    axis_tag = models.CharField(
        max_length=100,
        verbose_name=_("Axis Tag"),
        help_text=_("Label or identifier for the grid axis.")
    )
    axis_curve = models.ForeignKey(
        IfcCurve,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Axis Curve"),
        help_text=_("Geometric curve associated with the grid axis.")
    )

    # same_sense = models.BooleanField(
    #     default=True,
    #     verbose_name=_("Same Sense"),
    #     help_text=_("Indicates if the grid axis has the same sense as the geometric representation.")
    # )

    same_sense = IfcBooleanmdelField(
        default = 1,
        verbose_name=_("Same Sense"),
        help_text=_("Indicates if the grid axis has the same sense as the geometric representation.")
    )


    class Meta:
        verbose_name = _("IFC Grid Axis")
        verbose_name_plural = _("IFC Grid Axes")

    # Class | Model Methods
    # =========================================================================

    def __str__(self) -> str:
        """
        """
        return f"{self.axis_tag} (Same Sense: {'Yes' if self.same_sense else 'No'})"


# =============================================================================
# Module Variables
# =============================================================================

__all__ = [
    "IfcGridAxisModel",
]


