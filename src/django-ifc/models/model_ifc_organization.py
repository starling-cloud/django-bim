# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Organization Model Class
=====================================


For more information, refer to:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcactorresource/lexical/ifcorganization.htm

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
from ..fields.model import (
    # IfcGloballyUniqueIdField,
    IfcIdentifierField,
    IfcLabelField,
    IfcTextField,
)


# =============================================================================
# Variables
# =============================================================================

__all__ = ["IfcOrganizationModel", ]


# =============================================================================
# Classes
# =============================================================================

class IfcOrganizationModel(models.Model):
    """
    IFC Organization Model Class
    ============================

    Represents an IfcOrganization as defined by the IFC standards.

    Captures essential details about organizations participating in various
    capacities within construction projects. These include their name,
    a unique identifier, their roles, and a description of their activities.

    Attributes:
        identifier (IfcIdentifierField): A unique identifier for the
            organization, such as a registration number. Allows null and
            blank for flexibility.
        name (IfcLabelField): The official name of the organization. Allows
            null and blank.
        description (IfcTextField): Additional information about the
            organization. Allows null and blank.
        roles (ManyToManyField): Associations to different roles the
            organization might perform within the construction process, as
            defined in a separate `IfcRoleModel`.

    """

    identifier = IfcIdentifierField(
        unique=True,
        blank=True,
        null=True,
        verbose_name=_("Identifier"),
        help_text=_("A unique identifier for the organization, such as a registration number.")  # noqa E501
    )

    name = IfcLabelField(
        blank=True,
        null=True,
        verbose_name=_("Organization Name"),
        help_text=_("The official name of the organization.")
    )

    description = IfcTextField(
        blank=True,
        null=True,
        verbose_name=_("Description"),
        help_text=_("A brief description of the organization.")
    )

    roles = models.ManyToManyField(
        'IfcRoleModel',
        verbose_name=_("Roles"),
        help_text=_("Roles that the organization performs in the construction process."),  # noqa E501
        blank=True
    )

    def __str__(self) -> str:
        return self.name or _("Unnamed Organization")

    class Meta:
        verbose_name = _("IfcOrganization")
        verbose_name_plural = _("IfcOrganizations")
        indexes = [
            # Indexing on identifier to improve lookup performance.
            models.Index(fields=['identifier']),
        ]