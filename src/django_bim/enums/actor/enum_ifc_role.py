# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Role Enum Class
============================

This module defines an enumeration class `IfcRoleEnum` according to the
IFC standard, detailing various roles that can be assigned to actors
in a building construction project. These roles are essential for categorizing
job functions and responsibilities within IFC data models and can be used
to align project staffing and organization structures with IFC-compliant
systems.

For more information, refer to:
- https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcRoleEnum.htm
- https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcactorresource/lexical/ifcroleenum.htm

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
from enum import Enum
# from typing import Any, Dict, List

# Import | Libraries
from django.utils.translation import gettext_lazy as _

# Import | Local Modules


# =============================================================================
# Classes
# =============================================================================

class IfcRoleEnum(Enum):
    """
    IFC Role Enum Class
    ===================

    Enumeration for IfcRoleEnum providing standardized role types as specified
    in the IFC standard.

    Each enum member represents a role type that can be assigned to actors
    involved in building construction projects, ensuring adherence to
    international standards for classification and reporting.

    Examples:
        - ARCHITECT: Responsible for design and aesthetics.
        - ENGINEER: Can be specialized into categories such as CIVILENGINEER
            or STRUCTURALENGINEER.
        - CONTRACTOR: Primary entity responsible for the construction phase.

    """

    # Class | Enum Members
    # =========================================================================

    ARCHITECT = _("Architect")
    BUILDINGOPERATOR = _("Building Operator")
    BUILDINGOWNER = _("Building Owner")
    CIVILENGINEER = _("Civil Engineer")
    CLIENT = _("Client")
    COMMISSIONINGENGINEER = _("Commissioning Engineer")
    CONSTRUCTIONMANAGER = _("Construction Manager")
    CONSULTANT = _("Consultant")
    CONTRACTOR = _("Contractor")
    COSTENGINEER = _("Cost Engineer")
    ELECTRICALENGINEER = _("Electrical Engineer")
    ENGINEER = _("Engineer")
    FACILITIESMANAGER = _("Facilities Manager")
    FIELDCONSTRUCTIONMANAGER = _("Field Construction Manager")
    MANUFACTURER = _("Manufacturer")
    MECHANICALENGINEER = _("Mechanical Engineer")
    OWNER = _("Owner")
    PROJECTMANAGER = _("Project Manager")
    RESELLER = _("Reseller")
    STRUCTURALENGINEER = _("Structural Engineer")
    SUBCONTRACTOR = _("Sub-contractor")
    SUPPLIER = _("Supplier")
    USERDEFINED = _("User Defined")

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
        Provides Django-compatible choices for model fields.

        This method is particularly useful when using this Enum class in a
        Django model as the choices for a field, facilitating the integration
        of standardized role data into Django forms and admin interfaces.

        Returns:
            tuple of tuples: Each tuple contains the enum member's name and its
                localized human-readable value, suitable for use in model
                field choices.
        """
        try:
            return tuple(
                (item.name, item.value) for item in cls
            )
        except Exception as e:
            # Handle the error, log it, or raise a custom exception if
            # necessary
            raise ValueError(
                "Failed to generate choices from the Enum: {}".format(e)
            )


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "IfcRoleEnum",
]
