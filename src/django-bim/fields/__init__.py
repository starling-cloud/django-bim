# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Django BIM Fields Module
========================

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
from .model import (
    IfcGloballyUniqueIdField,
    IfcLabelField,
    IfcTextField,
)


# =============================================================================
# Module Level Variables
# =============================================================================

__all__ = [
    "IfcGloballyUniqueIdField",
    "IfcLabelField",
    "IfcTextField",
]
