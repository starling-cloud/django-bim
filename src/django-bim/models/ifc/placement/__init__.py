# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Django BIM IFC Placement Models Module
======================================

This module contains Django models for representing various types of object
placements in Building Information Modeling (BIM) using the Industry
Foundation Classes (IFC) schema. It provides models for different placement
strategies, including:

- `IfcGridPlacementModel`: Handles placements based on grid structures,
    typical in layout and architectural planning.
- `IfcLocalPlacementModel`: Manages local placement definitions, allowing
    objects to be placed relative to other objects.
- `IfcObjectPlacementModel`: Serves as the abstract base class for defining
    the general placement logic used by all specific placement models.

These models facilitate the integration and manipulation of spatial data
within Django, adhering to the IFC standards.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Local Modules
from .model_ifc_placement_grid import IfcGridPlacementModel
from .model_ifc_placement_local import IfcLocalPlacementModel
from .model_ifc_placement_object import IfcObjectPlacementModel


# =============================================================================
# Module Level Variables
# =============================================================================

__all__ = [
    "IfcGridPlacementModel",
    "IfcLocalPlacementModel",
    "IfcObjectPlacementModel",
]
