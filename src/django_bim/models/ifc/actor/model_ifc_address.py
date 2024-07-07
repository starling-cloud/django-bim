# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Address Model Class
================================


For more information, refer to:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcactorresource/lexical/ifcaddress.htm

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
    IfcTextField,
)
from ...enums import IfcAddressTypeEnum


# =============================================================================
# Variables
# =============================================================================


# =============================================================================
# Classes
# =============================================================================

class IfcAddressModel(models.Model):
    """
    IFC Address Model Class
    =======================

    Model representing an IfcAddress as defined in the IFC standard.

    This model is capable of representing various types of addresses including
    physical, postal, telecom, and email addresses in accordance with the
    specifications provided in the IFC standards.

    Attributes:
        purpose (CharField): The intended purpose of this address, based on
            IfcAddressTypeEnum.
        description (TextField): Additional description or notes about
            the address.
        user_defined_purpose (CharField): Allows specification of a
            non-standard purpose, if 'USERDEFINED' is chosen.
        of_organization (ForeignKey): Link to the organization this address
            belongs to.
        of_person (ForeignKey): Link to the person this address belongs to.

    """

    # Class | Model Fields
    # =========================================================================

    purpose = models.CharField(
        max_length = 50,
        choices = IfcAddressTypeEnum.choices(),
        default = IfcAddressTypeEnum.NOTDEFINED.name,
        verbose_name = _("Purpose"),
        help_text = _(
            "The intended purpose of this address, according to IfcAddressTypeEnum."  # noqa E501
        )
    )

    description = IfcTextField(
        blank = True,
        null = True,
        verbose_name = _("Description"),
        help_text = _("Additional description or notes about the address.")
    )

    user_defined_purpose = IfcLabelField(
        blank = True,
        null = True,
        verbose_name = _("User Defined Purpose"),
        help_text = _(
            "Specify the purpose if 'USERDEFINED' is selected in 'purpose'."  # noqa E501
        )
    )

    # of_organization = models.ForeignKey(
    #     'IfcOrganization',
    #     on_delete=models.CASCADE,
    #     related_name='addresses',
    #     null=True,
    #     blank=True,
    #     verbose_name=_("Organization"),
    #     help_text=_("The organization this address is associated with.")
    # )

    # of_person = models.ForeignKey(
    #     'IfcPerson',
    #     on_delete=models.CASCADE,
    #     related_name='addresses',
    #     null=True,
    #     blank=True,
    #     verbose_name=_("Person"),
    #     help_text=_("The person this address is associated with.")
    # )

    # Class | Model Meta Class
    # =========================================================================

    class Meta:
        """
        Meta Class
        ----------

        """
        verbose_name = _("IFC Address")
        verbose_name_plural = _("IFC Addresses")

    # Class | Model Methods
    # =========================================================================

    def __str__(self) -> str:
        """
        """
        return f"{self.purpose}: {self.description[:50]}..." if self.description else self.purpose  # noqa E501


# =============================================================================
# Module Variables
# =============================================================================

__all__ = [
    "IfcAddressModel",
]
