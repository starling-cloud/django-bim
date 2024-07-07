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

__all__ = ["IfcRepresentationItemModel", ]


# =============================================================================
# Classes
# =============================================================================

class IfcRepresentationItemModel(models.Model):
    """
    IFC Representation Item Model Class
    ===================================

    Abstract Django model representing an IfcRepresentationItem, which is
    defined in the IFC 2x3 standard as the abstract supertype of all geometric
    and topological representation items within a representation.

    This model is abstract and should be inherited by specific models that
    implement detailed geometric or topological structures.

    Attributes:
        name (CharField): Optional name of the representation item.

    """

    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Name"),
        help_text=_("Optional name of the representation item.")
    )

    class Meta:
        abstract = True  # Makes this model an abstract base class

    def __str__(self):
        return self.name if self.name else super().__str__()
