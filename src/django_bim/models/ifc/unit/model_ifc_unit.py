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

https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcmeasureresource/lexical/ifcunit.htm

from django.db import models
from django.utils.translation import gettext_lazy as _

class IfcUnit(models.Model):
    """
    Abstract Django model representing an IfcUnit, as defined in the IFC 2x3 standard.
    
    This is an abstract model that serves as a base for different types of units of measurement
    used within an IFC model, such as length, area, volume, and more.

    Attributes:
        unit_type (CharField): The type of the unit, e.g., LENGTHUNIT, AREAUNIT, etc.
    """

    # Enum or Choices for unit types could be defined here if needed
    UNIT_TYPES = (
        ('LENGTHUNIT', _('Length Unit')),
        ('AREAUNIT', _('Area Unit')),
        ('VOLUMEUNIT', _('Volume Unit')),
        ('COUNTUNIT', _('Count Unit')),
        ('WEIGHTUNIT', _('Weight Unit')),
        ('TIMEUNIT', _('Time Unit')),
    )

    unit_type = models.CharField(
        max_length=50,
        choices=UNIT_TYPES,
        verbose_name=_("Unit Type"),
        help_text=_("Specifies the type of unit of measure.")
    )

    # Class | Model Meta Class
    # =========================================================================

    class Meta:
        """
        Meta Class
        ----------

        """
        abstract = True  # This makes sure the class is not created as a table in the database

    # Class | Model Methods
    # =========================================================================

    def __str__(self) -> str:
        """
        """
        return f"{self.get_unit_type_display()}"


# =============================================================================
# Module Variables
# =============================================================================

__all__ = [
    "IfcActorRoleModel",
]
