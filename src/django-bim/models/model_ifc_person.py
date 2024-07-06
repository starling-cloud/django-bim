# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Person Model Class
===============================

This Django model encapsulates an individual's detailed information,
adhering to the IFC 2x3 standard for representing persons involved in
building projects. It covers personal identification, names, titles,
roles, and addresses.

For more information, refer to:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcactorresource/lexical/ifcperson.htm

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

__all__ = ["IfcPersonModel", ]


# =============================================================================
# Classes
# =============================================================================

class IfcPersonModel(models.Model):
    """
    IFC Person Model Class
    ======================

    Represents an IfcPerson as defined by the IFC 2x3 standard.

    This model handles personal details necessary for identifying individuals
    participating in construction projects. It facilitates the management of
    their roles and contact information within the project's ecosystem.

    Attributes:
        identifier (IfcIdentifierField): A unique and potentially nullable
            identifier for the person.
        last_name (IfcLabelField): The individual's last name.
        first_name (IfcLabelField): The individual's first name.
        middle_names (IfcLabelField): Any middle names of the individual.
        prefix_titles (IfcLabelField): Titles preceding the name,
            e.g., Mr., Dr.
        suffix_titles (IfcLabelField): Titles following the name,
            e.g., Jr., PhD.
        roles (ManyToManyField): Various roles the person may hold within
            projects.
        addresses (ManyToManyField): Linked addresses for the individual.

    """

    identifier = IfcIdentifierField(
        unique=True,
        blank=True,
        null=True,
        verbose_name=_("Identification"),
        help_text=_(
            "A unique identifier for the person, such as an employee or membership number."  # noqa E501
        )
    )

    last_name = IfcLabelField(
        blank=True,
        null=True,
        verbose_name=_("Last Name"),
        help_text=_("The individual's surname or family name.")
    )

    first_name = IfcLabelField(
        blank=True,
        null=True,
        verbose_name=_("First Name"),
        help_text=_("The individual's given name.")
    )

    middle_names = IfcLabelField(
        blank=True,
        null=True,
        verbose_name=_("Middle Names"),
        help_text=_("Any middle names of the individual.")
    )

    prefix_titles = IfcLabelField(
        blank=True,
        null=True,
        verbose_name=_("Prefix Titles"),
        help_text=_(
            "Honorifics or formal titles preceding the individual's name."
        )
    )

    suffix_titles = IfcLabelField(
        blank=True,
        null=True,
        verbose_name=_("Suffix Titles"),
        help_text=_(
            "Qualifications or titles following the individual's name."
        )
    )

    roles = models.ManyToManyField(
        'IfcRoleModel',
        verbose_name=_("Roles"),
        help_text=_(
            "The roles held by the individual within various projects."
        ),
        blank=True
    )

    addresses = models.ManyToManyField(
        'IfcAddressModel',
        verbose_name=_("Addresses"),
        help_text=_("The individual's contact addresses."),
        blank=True
    )

    def __str__(self):
        """
        Provide a human-readable string representation of the person.
        """
        parts = [
            self.prefix_titles,
            self.first_name,
            self.middle_names,
            self.last_name,
            self.suffix_titles
        ]
        # Efficiently concatenate non-empty name parts

        return " ".join(part for part in parts if part)

    class Meta:
        verbose_name = _("IfcPerson")
        verbose_name_plural = _("IfcPersons")
        # Default ordering by last name then first name for easier navigation
        ordering = ['last_name', 'first_name']
