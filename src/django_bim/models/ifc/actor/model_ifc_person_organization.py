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
        on_delete = models.CASCADE,
        verbose_name = _("Person"),
        help_text = _("The individual associated with the organization."),
    )

    organization = models.ForeignKey(
        "IfcOrganizationModel",
        on_delete = models.CASCADE,
        verbose_name = _("Organization"),
        help_text = _(
            "The organization with which the person is associated."
        ),
    )

    roles = models.ManyToManyField(
        "IfcRoleModel",
        blank=True,
        verbose_name = _("Roles"),
        help_text = _(
            "Specific roles the person fulfills within the organization."
        ),
    )

    # Class | Model Meta Class
    # =========================================================================

    class Meta:
        """
        Meta Class
        ----------

        """
        verbose_name = _("IFC Person and Organization")
        verbose_name_plural = _("IFC Persons and Organizations")
        # Ensures each combination of person and organization is unique
        unique_together = (
            "person",
            "organization",
        )

    # Class | Model Methods
    # =========================================================================

    def __str__(self) -> str:
        """
        """
        return f"{self.person} at {self.organization}"


# =============================================================================
# Module Variables
# =============================================================================

__all__ = [
    "IfcPersonAndOrganizationModel",
]
