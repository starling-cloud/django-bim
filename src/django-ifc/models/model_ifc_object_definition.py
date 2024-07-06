# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Object Definition Model Class
=========================================

This Django model class serves as an abstract base for all object definitions
according to the IFC 2x3 standard. It encapsulates common attributes and
behaviors that are inherited by more specific IFC entity models, facilitating
generic metadata management and object relationships.

This model enhances the IfcRootModel by adding or refining functionality
specific to object definitions.

For detailed specifications, see:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifckernel/lexical/ifcobjectdefinition.htm

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
# from uuid import uuid4
# from typing import Any, Dict, List

# Import | Libraries
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Import | Local Modules
from .model_ifc_root import IfcRootModel


# =============================================================================
# Variables
# =============================================================================

__all__ = ["IfcObjectDefinitionModel", ]


# =============================================================================
# Classes
# =============================================================================

class IfcObjectDefinitionModel(IfcRootModel):
    """
    IFC Object Definition Model Class
    ================================

    Abstract model representing an IfcObjectDefinition as defined in the
    IFC 2x3 standard.

    This class provides a framework for all derived IFC object models and
    includes mechanisms for generic metadata management and establishing
    relationships within the IFC data schema.

    Attributes inherited from IfcRootModel:
        global_id (IfcGloballyUniqueIdField): Globally unique identifier.
        name (IfcLabelField): The name of the object, allowing null.
        description (IfcTextField): A textual description of the object,
            allowing null.
        owner_history (ForeignKey to IfcOwnerHistory): Ownership history of
            the object.

    """

    class Meta(IfcRootModel.Meta):
        abstract = True  # Ensuring this remains an abstract model

    def __str__(self):
        """
        Provide a more informative string for representing this object
        in the admin or logs.
        """
        return self.name if self.name else _("Unnamed IFC Object")

    def get_absolute_url(self):
        """
        Generate the absolute URL for an object instance (useful for admin
        or detail views).
        """
        return reverse('ifc_object_definition_detail', kwargs={'pk': self.pk})
