# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Person Organization Model Class
============================================


For more information, refer to:


"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library

# Import | Libraries
from typing import Literal

from django.db import models
from django.utils.translation import gettext_lazy as _

# Import | Local Modules


# =============================================================================
# Variables
# =============================================================================


# =============================================================================
# Classes
# =============================================================================


class IfcPersonAndOrganizationModel(models.Model):
    """
    IFC Person Organization Model Class
    ===================================

    Model representing an IfcPersonAndOrganization as defined in the
    IFC standard.

    This model links individuals (IfcPerson) with organizations
    (IfcOrganization), capturing their associations within the context of
    building projects.

    Attributes:
        person (ForeignKey): The individual involved in the organization.
        organization (ForeignKey): The organization with which the person
            is associated.
        roles (ManyToManyField): Specific roles the person fulfills within
            the organization.
    """

    # Class | Model Fields
    # =========================================================================

    person = models.ForeignKey(
        "IfcPersonModel",
        on_delete=models.CASCADE,
        verbose_name=_(message="Person"),
        help_text=_(
            message="The individual associated with the organization."
        ),
    )

    organization = models.ForeignKey(
        "IfcOrganizationModel",
        on_delete=models.CASCADE,
        verbose_name=_(message="Organization"),
        help_text=_(
            message="The organization with which the person is associated."
        ),
    )

    roles = models.ManyToManyField(
        "IfcRoleModel",
        blank=True,
        verbose_name=_(message="Roles"),
        help_text=_(
            message="Specific roles the person fulfills within the organization."
        ),
    )

    # Class | Model Meta Class
    # =========================================================================

    class Meta:
        """
        Meta Class
        ----------

        """

        verbose_name: str = _(message="IFC Person and Organization")
        verbose_name_plural: str = _(message="IFC Persons and Organizations")
        # Ensures each combination of person and organization is unique
        unique_together: tuple[Literal["person"], Literal["organization"]] = (
            "person",
            "organization",
        )

    # Class | Model Methods
    # =========================================================================

    def __str__(self) -> str:
        """ """
        return f"{self.person} at {self.organization}"


# =============================================================================
# Module Variables
# =============================================================================

__all__: list[str] = [
    "IfcPersonAndOrganizationModel",
]
