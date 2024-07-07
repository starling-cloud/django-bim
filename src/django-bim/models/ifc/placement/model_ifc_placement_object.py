# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Object Placement Model Class
=========================================

For more information, refer to:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcgeometricconstraintresource/lexical/ifcobjectplacement.htm

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library

# Import | Libraries
from django.db import models
from django.utils.translation import gettext_lazy as _

# Import | Local Modules
from ....fields.model import (
    IfcLabelField,
    IfcRoleTypeField,
    IfcTextField,
)


# =============================================================================
# Classes
# =============================================================================

class IfcObjectPlacementModel(models.Model):
    """
    Abstract Django model representing an IfcObjectPlacement as defined in
    the IFC standard.

    This model provides a basis for spatial location and orientation of
    objects, acting as an abstract supertype for all positioning entities.

    Attributes:
        placement_id (CharField): A unique identifier for the placement.
    """

    # Class | Model Fields
    # =========================================================================

    # optional
    placement_id = models.CharField(
        max_length = 255,
        unique = True,
        verbose_name = _("Placement ID"),
        help_text = _("A unique identifier for the placement.")
    )

    # Class | Model Meta Class
    # =========================================================================

    class Meta:
        """
        Meta Class
        ----------

        """
        abstract = True  # This model will not be created in the database
        verbose_name = _("IFC Object Placement")
        verbose_name_plural = _("IFC Object Placements")

    # Class | Model Methods
    # =========================================================================

    def __str__(self) -> str:
        """
        """
        return f"Placement ID: {self.placement_id}"


# =============================================================================
# Module Variables
# =============================================================================

__all__ = [
    "IfcObjectPlacementModel",
]
