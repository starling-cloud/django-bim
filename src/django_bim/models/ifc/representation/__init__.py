# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Django BIM IFC Representation Models Module
===========================================



"""


# =============================================================================
# Imports
# =============================================================================

# Import | Local Modules
from .model_ifc_representation import IfcRepresentationModel
from .model_ifc_representation_context import IfcRepresentationContextModel
from .model_ifc_representation_item import IfcRepresentationItemModel
from .model_ifc_representation_item_geometric import IfcGeometricRepresentationItemModel
from .model_ifc_representation_map import IfcGeometricRepresentationMapModel


# =============================================================================
# Module Level Variables
# =============================================================================

__all__ = [
    "IfcRepresentationModel",
    "IfcRepresentationContextModel",
    "IfcRepresentationItemModel",
    "IfcGeometricRepresentationItemModel",
    "IfcGeometricRepresentationMapModel",
]
