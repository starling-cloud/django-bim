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

https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifckernel/lexical/ifcproduct.htm

class IfcProductModel(IfcObjectDefinition):
    """
    Django model representing an IfcProduct as defined in the IFC standard.

    IfcProduct is the base class for all physical elements that have a physical manifestation
    and can be spatially located and oriented.

    Attributes:
        object_placement (ForeignKey): Specifies the placement of the product in space.
        representation (ForeignKey): Links to the geometric and/or topological representation of the product.
    """

    object_placement = models.ForeignKey(
        IfcObjectPlacement,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Object Placement"),
        help_text=_("Specifies the placement of the product in space.")
    )

    representation = models.ForeignKey(
        IfcProductRepresentation,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Representation"),
        help_text=_(
            "Links to the geometric and/or topological representation of the product."
        )
    )

    # Class | Model Meta Class
    # =========================================================================

    class Meta:
        """
        Meta Class
        ----------

        """
        verbose_name = _("IFC Product")
        verbose_name_plural = _("IFC Products")

    def __str__(self) -> str:
        """
        """
        return f"{self.name} - Placement: {self.object_placement}, Representation: {self.representation}"


# =============================================================================
# Module Variables
# =============================================================================

__all__ = [
    "IfcProductModel",
]
