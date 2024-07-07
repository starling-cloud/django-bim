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

class LengthUnit(IfcUnit):
    """
    Concrete model representing a specific type of IfcUnit for length measurements.

    Attributes:
        unit_name (CharField): The name of the length unit, e.g., meter, millimeter.
    """

    unit_name = models.CharField(
        max_length=100,
        verbose_name=_("Unit Name"),
        help_text=_("Name of the length unit, e.g., meter, millimeter.")
    )

    # Class | Model Meta Class
    # =========================================================================

    class Meta:
        """
        Meta Class
        ----------

        """
        verbose_name = _("Length Unit")
        verbose_name_plural = _("Length Units")

    # Class | Model Methods
    # =========================================================================

    def __str__(self) -> str:
        """
        """
        return f"{self.unit_name}"

# =============================================================================
# Module Variables
# =============================================================================

__all__ = [
    "IfcActorRoleModel",
]
