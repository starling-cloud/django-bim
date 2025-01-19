# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Person Model Class
===============================

This Django model encapsulates an individual's detailed information,
adhering to the IFC standard for representing persons involved in
building projects. It covers personal identification, names, titles,
roles, and addresses.

For more information, refer to:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcactorresource/lexical/ifcperson.htm

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library

# Import | Libraries
from django.db import models
from django.utils.translation import gettext_lazy as _

# Import | Local Modules
from ....fields.model import IfcIdentifierField, IfcLabelField

# =============================================================================
# Variables
# =============================================================================


# =============================================================================
# Classes
# =============================================================================


class IfcPersonModel(models.Model):
    """
    IFC Person Model Class
    ======================

    Represents an IfcPerson as defined by the IFC standard.

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

    # Class | Model Fields
    # =========================================================================

    identifier = IfcIdentifierField(
        unique=True,
        blank=True,
        null=True,
        verbose_name=_(message="Identification"),
        help_text=_(
            message="Identification of the person."
            "A unique identifier for the person, such as an employee or membership number."  # noqa E501
        ),
    )

    family_name = IfcLabelField(
        blank=True,
        null=True,
        verbose_name=_(message="Family Name"),
        help_text=_(
            message="The name by which the family identity of the person may be recognized."  # noqa E501
        ),
    )

    first_name = IfcLabelField(
        blank=True,
        null=True,
        verbose_name=_(message="First Name"),
        help_text=_(message="The individual's given name."),
    )

    middle_names = IfcLabelField(
        blank=True,
        null=True,
        verbose_name=_(message="Middle Names"),
        help_text=_(message="Any middle names of the individual."),
    )

    prefix_titles = IfcLabelField(
        blank=True,
        null=True,
        verbose_name=_(message="Prefix Titles"),
        help_text=_(
            message="Honorifics or formal titles preceding the individual's name."
        ),
    )

    suffix_titles = IfcLabelField(
        blank=True,
        null=True,
        verbose_name=_(message="Suffix Titles"),
        help_text=_(
            message="Qualifications or titles following the individual's name."
        ),
    )

    roles = models.ManyToManyField(
        to="IfcRoleModel",
        blank=True,
        verbose_name=_(message="Roles"),
        help_text=_(
            message="The roles held by the individual within various projects."
        ),
    )

    addresses = models.ManyToManyField(
        "IfcAddressModel",
        blank=True,
        verbose_name=_(message="Addresses"),
        help_text=_(message="The individual's contact addresses."),
    )

    class Meta:
        """
        Meta Class
        ----------

        """

        verbose_name: str = _(message="IFC Person")
        verbose_name_plural: str = _(message="IFC Persons")
        # Default ordering by last name then first name for easier navigation
        ordering: list[str] = [
            "last_name",
            "first_name",
        ]

    # Class | Model Methods
    # =========================================================================

    def __str__(self) -> str:
        """
        Provide a human-readable string representation of the person.
        """
        parts = [
            self.prefix_titles,
            self.first_name,
            self.middle_names,
            self.last_name,
            self.suffix_titles,
        ]
        # Efficiently concatenate non-empty name parts

        return " ".join(part for part in parts if part)


# =============================================================================
# Module Variables
# =============================================================================

__all__: list[str] = [
    "IfcPersonModel",
]
