# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Organization Model Class
=====================================

This model represents an organization as defined in the IFC 2x3 standard,
encompassing entities involved in construction projects. This model captures
crucial details such as the organization's name, unique identifier, roles
within construction projects, and their addresses.

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

    Represents an IfcOrganization as defined by IFC standards, detailing
    organizations involved in various capacities within construction projects.

    Attributes:
        identifier (IfcIdentifierField): A unique, optionally nullable
            identifier for the organization.
        name (IfcLabelField): The formal name of the organization, which can
            also be left unspecified.
        description (IfcTextField): Descriptive text about the organization's
            function or structure.
        roles (ManyToManyField): Links to defined roles the organization
            fulfills in the construction process.
        address (ManyToManyField): Links to addresses associated with the
            organization, covering both physical and electronic forms of
            contact.
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

    address = models.ManyToManyField(
        'IfcAddressModel',
        verbose_name=_("Addresses"),
        help_text=_("Postal and telecom addresses of an organization."),
        blank=True
    )

    def __str__(self) -> str:
        """
        Provides a human-readable representation of the organization,
        defaulting to a placeholder if the name is unspecified.
        """
        return self.name or _("Unnamed Organization")

    class Meta:
        verbose_name = _("IFC Organization")
        verbose_name_plural = _("IFC Organizations")
        indexes = [
            models.Index(fields=['identifier'], name='idx_ifc_organization_identifier')  # noqa E501
        ]
