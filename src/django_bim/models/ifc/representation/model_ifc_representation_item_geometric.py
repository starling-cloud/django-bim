# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Geometric Representation Item Model Class
============================================


For detailed specifications, see:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcgeometryresource/lexical/ifcgeometricrepresentationitem.htm

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
# from uuid import uuid4
# from typing import Any, Dict, List

# Import | Libraries
from django.db import models
from django.utils.translation import gettext_lazy as _

# Import | Local Modules


# =============================================================================
# Variables
# =============================================================================


# =============================================================================
# Classes
# =============================================================================

class IfcGeometricRepresentationItemModel(models.Model):
    """
    IFC Geometric Representation Item Model Class
    ===================================

    Abstract Django model representing an IfcGeometricRepresentationItem as defined in the IFC standard.

    This is the base class for all geometric representation items, which are components of geometric models
    in building information modeling.

    Attributes:
        representation_identifier (CharField): An optional identifier for the geometric representation item.

    """

    # Class | Model Fields
    # =========================================================================

    representation_identifier = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Representation Identifier"),
        help_text=_("An optional identifier for the geometric representation item.")
    )

    # Class | Model Meta Class
    # =========================================================================

    class Meta:
        """
        Meta Class
        ----------

        """
        abstract = True  # This model will not be created in the database
        verbose_name = _("IFC Geometric Representation Item")
        verbose_name_plural = _("IFC Geometric Representation Items")

    # Class | Model Methods
    # =========================================================================

    def __str__(self) -> str:
        """
        """
        return self.representation_identifier if self.representation_identifier else super().__str__()


# =============================================================================
# Module Variables
# =============================================================================

__all__ = [
    "IfcGeometricRepresentationItem",
]
