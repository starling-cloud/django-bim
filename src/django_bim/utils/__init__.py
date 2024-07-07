# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Django BIM Utils Module
=======================

This module provides utility functions and classes that facilitate the
handling of Industry Foundation Classes (IFC) data within a Django
application. It includes functions for validating IFC data types and
potentially other common operations that are useful across various parts
of the application when dealing with IFC standards.

Available Functions:
- validate_ifc_guid: Validates that a string conforms to the 22-character
  Base64 requirement of IfcGloballyUniqueId, ensuring it is suitable for use
  as an IFC GUID.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Local Modules
from .validate_ifc_guid import validate_ifc_guid


# =============================================================================
# Module Level Variables
# =============================================================================

__all__ = ['validate_ifc_guid', ]
