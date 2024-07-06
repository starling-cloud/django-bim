# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Role Enum Class
============================

This module defines an enumeration class `IfcRoleEnum` according to the
IFC 2x3 standard, detailing various roles that can be assigned to actors
in a building construction project. This is particularly useful for
categorizing job functions and responsibilities in IFC data models.

For more information, refer to:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcactorresource/lexical/ifcroleenum.htm

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

    Enumeration for IfcRoleEnum providing role types as specified in the
    IFC 2x3 standard.

    Each enum member represents a role type that can be assigned to actors
    involved in building construction projects, ensuring adherence to
    international standards for classification and reporting.

    Examples include roles like 'ARCHITECT', 'ENGINEER', and 'CONTRACTOR',
    among others.

    """

    SUPPLIER = _('Supplier')
    MANUFACTURER = _('Manufacturer')
    CONTRACTOR = _('Contractor')
    SUBCONTRACTOR = _('Subcontractor')
    ARCHITECT = _('Architect')
    STRUCTURALENGINEER = _('Structural Engineer')
    COSTENGINEER = _('Cost Engineer')
    CLIENT = _('Client')
    BUILDINGOWNER = _('Building Owner')
    BUILDINGOPERATOR = _('Building Operator')
    MECHANICALENGINEER = _('Mechanical Engineer')
    ELECTRICALENGINEER = _('Electrical Engineer')
    PROJECTMANAGER = _('Project Manager')
    FACILITIESMANAGER = _('Facilities Manager')
    CIVILENGINEER = _('Civil Engineer')
    COMMISSIONINGENGINEER = _('Commissioning Engineer')
    ENGINEER = _('Engineer')
    OWNER = _('Owner')
    CONSULTANT = _('Consultant')
    CONSTRUCTIONMANAGER = _('Construction Manager')
    FIELDCONSTRUCTIONMANAGER = _('Field Construction Manager')
    RESELLER = _('Reseller')
    USERDEFINED = _('User Defined')

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
        return tuple((item.name, item.value) for item in cls)


# =============================================================================
# Module Level Variables
# =============================================================================

__all__ = ["IfcRoleEnum", ]
