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

https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcmeasureresource/lexical/ifcunitassignment.htm

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _

class IfcUnitAssignment(models.Model):
    """
    Model representing an IfcUnitAssignment as defined in the IFC 2x3 standard.

    This model is used to define the units of measurement used across a project, relating to various specific unit types.
    """

    # Generic relation to associate any type of IfcUnit
    units = GenericRelation(
        'IfcUnitRelation',
        related_query_name='unit_assignments',
        verbose_name=_("Units"),
        help_text=_("Collection of units used throughout the project.")
    )

    # Class | Model Meta Class
    # =========================================================================

    class Meta:
        """
        Meta Class
        ----------

        """

    # Class | Model Methods
    # =========================================================================

    def __str__(self) -> str:
        """
        """
        return f"Unit Assignment {self.pk}"


# =============================================================================
# Module Variables
# =============================================================================

__all__ = [
    "IfcActorRoleModel",
]
