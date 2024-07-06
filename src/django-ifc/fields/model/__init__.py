# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Django IFC Model Fields Module
==============================

This module provides custom Django model fields tailored to handle specific
data types used in the IFC (Industry Foundation Classes) standard for
building and construction data. These fields ensure compliance with IFC data
specifications, enabling more accurate data management and exchange within
Django applications.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Local Modules
from .field_model_ifc_guid import IfcGloballyUniqueIdField
from .field_model_ifc_identifier import IfcIdentifierField
from .field_model_ifc_label import IfcLabelField
from .field_model_ifc_text import IfcTextField


# =============================================================================
# Module Level Variables
# =============================================================================

__all__ = [
    "IfcGloballyUniqueIdField",
    "IfcIdentifierField",
    "IfcLabelField",
    "IfcTextField",
]
