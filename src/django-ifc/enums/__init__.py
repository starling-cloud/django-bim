# -*- coding: utf-8 -*-

"""
Django IFC Enums Module
=======================

This module provides enumeration classes that align with the IFC (Industry
Foundation Classes) standards. These enums are used throughout the Django IFC
application to ensure consistency and compliance with the predefined IFC
standards.

Currently, the module includes:
- `IfcAddressTypeEnum`: ...
- `IfcRoleEnum`: Enumerations for different roles specified in IFC standards
    that can be assigned to actors in a building construction project.

"""

# =============================================================================
# Imports
# =============================================================================

# Local enumeration modules
from .enum_ifc_address_type import IfcAddressTypeEnum
from .enum_ifc_role import IfcRoleEnum


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "IfcAddressTypeEnum",
    "IfcRoleEnum",
]
