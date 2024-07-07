# -*- coding: utf-8 -*-

"""
Django BIM Enums Module
=======================

This module provides enumeration classes that align with the IFC (Industry
Foundation Classes) standards. These enums are used throughout the Django BIM
application to ensure consistency and compliance with the predefined IFC
standards.

Currently, the module includes:
- `IfcAddressTypeEnum`: ...
- `IfcChangeActionEnum`: ...
- `IfcRoleEnum`: Enumerations for different roles specified in IFC standards
    that can be assigned to actors in a building construction project.
- `IfcStateEnum`: ...

"""

# =============================================================================
# Imports
# =============================================================================

# Local enumeration modules
from .enum_ifc_address_type import IfcAddressTypeEnum
from .enum_ifc_change_action import IfcChangeActionEnum
from .enum_ifc_role import IfcRoleEnum
from .enum_ifc_state import IfcStateEnum


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "IfcAddressTypeEnum",
    "IfcChangeActionEnum",
    "IfcRoleEnum",
    "IfcStateEnum",
]
