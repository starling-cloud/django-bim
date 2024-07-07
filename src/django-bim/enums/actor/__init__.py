# -*- coding: utf-8 -*-

"""
Django BIM IFC Actor Enums Module
==================================

This module provides enumerations related to actors in the Building
Information Modeling (BIM) context using IFC (Industry Foundation Classes)
standards. Enumerations are used to standardize the data fields in models,
ensuring that entries conform to predefined options, enhancing data integrity
and interoperability in construction and architectural projects.

Enumerations included:
- `IfcAddressTypeEnum`: Defines the types of addresses that can be used to
  specify location details in a structured manner. Examples include site
  addresses, home addresses, delivery points, etc.
- `IfcRoleEnum`: Enumerates different roles that can be assigned to actors
  within a building construction project, such as Architect, Engineer,
  Contractor, etc. This helps in defining clear responsibilities and
  permissions within project management systems.

These enums are particularly useful for developers working with Django models
that need to comply with IFC standards, providing a reliable and consistent
framework for data representation.

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
