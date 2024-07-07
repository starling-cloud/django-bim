# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Representation Item Model Class
============================================


For detailed specifications, see:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcgeometryresource/lexical/ifcrepresentationitem.htm

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

class IfcRepresentationItemModel(models.Model):
    """
    IFC Representation Item Model Class
    ===================================

    Abstract Django model representing an IfcRepresentationItem, which is
    defined in the IFC standard as the abstract supertype of all geometric
    and topological representation items within a representation.

    This model is abstract and should be inherited by specific models that
    implement detailed geometric or topological structures.

    Attributes:
        name (CharField): Optional name of the representation item.

    """

    # Class | Model Fields
    # =========================================================================

    # not part of specification?
    name = models.CharField(
        max_length = 255,
        blank = True,
        null = True,
        verbose_name = _("Name"),
        help_text = _("Optional name of the representation item."),
    )

    # Class | Model Meta Class
    # =========================================================================

    class Meta:
        """
        Meta Class
        ----------

        """
        abstract = True  # Makes this model an abstract base class

    # Class | Model Methods
    # =========================================================================

    def __str__(self) -> str:
        """
        """
        return self.name if self.name else super().__str__()


# =============================================================================
# Module Variables
# =============================================================================

__all__ = [
    "IfcRepresentationItemModel",
]
