# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Application Model Class
====================================

This module defines the IfcApplicationModel, which records details about the
software application used in the creation, modification, or interpretation of
IFC data models. This model is in accordance with the IFC 2x3 standard and
includes information about the application's developer, name, version, and a
unique identifier.

For more information, refer to:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcutilityresource/lexical/ifcapplication.htm

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
    # IfcTextField,
)


# =============================================================================
# Variables
# =============================================================================

__all__ = ["IfcApplicationModel", ]


# =============================================================================
# Classes
# =============================================================================

class IfcApplicationModel(models.Model):
    """
    IFC Application Model Class
    ===========================

    Model representing an IfcApplication, which is a component of the IFC
    standard used to record and reference the application software being used
    to generate the IFC model.

    This includes details about the application developer, software name,
    version identifier, and a unique application identifier.

    This model stores information about the software used to generate, modify,
    or analyze IFC models, facilitating documentation and standardization of
    application metadata.

    Attributes:
        application_developer (ForeignKey): Reference to the IfcOrganization
            responsible for the application.
        application_full_name (IfcLabelField): The official name of the
            application.
        application_identifier (IfcIdentifierField): A unique identifier for
            the application, often as a UUID.
        version (IfcLabelField): The software version detail.

    """

    application_developer = models.ForeignKey(
        'IfcOrganization',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='developed_applications',
        verbose_name=_("Application Developer"),
        help_text=_("Name of the organization or individual developing the application.")  # noqa E501
    )

    application_full_name = IfcLabelField(
        blank=True,
        null=True,
        verbose_name=_("Application Full Name"),
        help_text=_("Full name of the application software.")
    )

    application_identifier = IfcIdentifierField(
        unique=True,  # Ensuring uniqueness for each application identifier
        blank=True,
        null=True,
        verbose_name=_("Application Identifier"),
        help_text=_("A unique identifier for the application.")
    )

    version = IfcLabelField(
        blank=True,
        null=True,
        verbose_name=_("Version"),
        help_text=_("The version of the application software.")
    )

    def __str__(self) -> str:
        dev_name = self.application_developer.name if self.application_developer else "Unknown Developer"  # noqa E501
        return f"{self.application_full_name or 'Unnamed Application'} {self.version or 'v. Unknown'} by {dev_name}"  # noqa E501

    class Meta:
        verbose_name = _("IfcApplication")
        verbose_name_plural = _("IfcApplications")
        ordering = ['application_full_name', 'version']
