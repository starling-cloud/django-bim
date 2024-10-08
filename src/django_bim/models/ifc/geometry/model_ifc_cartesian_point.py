# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC ... Model Class
===================================

For more information, refer to:

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library

# Import | Libraries
from django.db import models
from django.utils.translation import gettext_lazy as _

# Import | Local Modules
from ...fields.model import (
    IfcLabelField,
    IfcRoleTypeField,
    IfcTextField,
)


# =============================================================================
# Classes
# =============================================================================

class IfcCartesianPoint(IfcRepresentationItem):
    """
    Model representing an IfcCartesianPoint, which defines a point in 2D or
    3D space by its coordinates.

    """

    x = models.FloatField(verbose_name=_("X Coordinate"))
    y = models.FloatField(verbose_name=_("Y Coordinate"))
    z = models.FloatField(blank=True, null=True, verbose_name=_("Z Coordinate"), help_text=_("Z coordinate is optional for 3D points."))


    # Class | Model Meta Class
    # =========================================================================

    # Class | Model Methods
    # =========================================================================

    def __str__(self) -> str:
        """
        """
        if self.z is not None:
            return f"Point({self.x}, {self.y}, {self.z})"
        return f"Point({self.x}, {self.y})"


# =============================================================================
# Module Variables
# =============================================================================

__all__ = [
    "IfcActorRoleModel",
]



class IfcCartesianPoint(IfcGeometricRepresentationItem):
    """
    Django model representing an IfcCartesianPoint, which is a type of IfcGeometricRepresentationItem.

    Represents a point defined by its coordinates in a Cartesian coordinate system.

    Attributes:
        coordinates (JSONField): Coordinates of the point.
    """

    coordinates = models.JSONField(
        verbose_name=_("Coordinates"),
        help_text=_("JSON representation of the Cartesian coordinates of the point.")
    )

    def __str__(self):
        return f"Cartesian Point: {self.coordinates}"