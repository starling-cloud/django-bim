# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Actor Role Model Class
===================================

This model represents the IfcActorRole as defined in the IFC standard,
detailing the roles played by different actors (e.g., individuals or
organizations) in construction projects.

For more information, refer to:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcactorresource/lexical/ifcactorrole.htm

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
    IfcRoleEnumField,
    IfcTextField,
)


# =============================================================================
# Classes
# =============================================================================

class IfcActorRoleModel(models.Model):
    """
    IFC Actor Role Model Class
    ==========================

    Model representing an IfcActorRole as defined in the IFC standard.

    This model captures the roles played by actors in construction projects.
    Each role can be predefined or user-defined, and includes a description.

    Attributes:
        role_type (CharField): Specifies the standard role type from IFC
            standards or 'USERDEFINED' if not listed.
        user_defined_role (IfcLabelField): Allows specification of a role not
            included in standard choices, applicable if role_type
            is 'USERDEFINED'.
        description (IfcTextField): Describes the responsibilities and duties
            associated with the role.
    """

    # Class | Model Fields
    # =========================================================================

    role = IfcRoleEnumField(
        verbose_name = _("Role"),
        help_text = _(
            "The role of the actor in the project according to IFC standards."
        ),
    )

    user_defined_role = IfcLabelField(
        blank = True,
        null = True,
        verbose_name = _("User Defined Role"),
        help_text = _(
            "A user-defined role, applicable if the role type is 'USERDEFINED'."  # noqa E501
        ),
    )

    description = IfcTextField(
        blank = True,
        null = True,
        verbose_name = _("Description"),
        help_text = _("A description of the role."),
    )

    # Class | Model Meta Class
    # =========================================================================

    class Meta:
        """
        Meta Class
        ----------

        """
        verbose_name = _("IFC Actor Role")
        verbose_name_plural = _("IFC Actor Roles")

    # Class | Model Methods
    # =========================================================================

    def __str__(self) -> str:
        """
        """
        if self.user_defined_role:
            return f"{self.user_defined_role} ({self.get_role_type_display()})"
        return self.get_role_type_display()


# =============================================================================
# Module Variables
# =============================================================================

__all__ = [
    "IfcActorRoleModel",
]
