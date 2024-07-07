# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Address Type Enum Class
====================================

This module defines the `IfcAddressTypeEnum` class, an enumeration of address
types according to the IFC standard. These address types are used to
categorize the addresses associated with entities like organizations or
persons involved in building projects. Proper use of these types ensures data
consistency across BIM applications.

For more information, refer to:
- https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcAddressTypeEnum.htm
- https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcactorresource/lexical/ifcaddresstypeenum.htm

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
from enum import Enum

# Import | Libraries
from django.utils.translation import gettext_lazy as _

# Import | Local Modules


# =============================================================================
# Classes
# =============================================================================

class IfcAddressTypeEnum(Enum):
    """
    IFC Address Type Enum Class
    ===========================

    Enumeration for IfcAddressTypeEnum providing address types according to
    the IFC standard.

    Each member of this enumeration represents a specific type of address
    that may be associated with various entities involved in a building
    project.

    Enum Members:
        - DISTRIBUTIONPOINT: An address used specifically for sending or
          receiving goods.
        - HOME: The residential address of an individual.
        - OFFICE: Typically the address of a business or administrative
          entity.
        - SITE: The location of a construction or project site.
        - USERDEFINED: A type specified by the user when standard types do
          not suffice.
        - NOTDEFINED: Used when the address type is not defined among the
          standard options.

    """

    # Class | Enum Members
    # =========================================================================

    DISTRIBUTIONPOINT = _("Distribution Point")
    HOME = _("Home")
    OFFICE = _("Office")
    SITE = _("Site")
    USERDEFINED = _("User Defined")
    NOTDEFINED = _("Not Defined")  # Not in specification

    # Class | Methods
    # =========================================================================

    def __str__(self) -> str:
        """
        Return the user-friendly name of the enum member, with error handling
        in case of unexpected value formats.
        """
        try:
            return self.value
        except ValueError as e:
            return str(e)  # Log the error or handle it appropriately

    @classmethod
    def choices(cls):
        """
        Returns the choices for field choices in a Django model field,
        formatted as required by Django's field choices.

        Returns:
            tuple of tuples: Each tuple contains the enum member's value and
                its human-readable name.

        """

        return tuple((item.name, item.value) for item in cls)


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "IfcAddressTypeEnum",
]
