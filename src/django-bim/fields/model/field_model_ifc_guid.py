# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC GUID Model Field Class
===================================

Defines a custom Django model field specifically for handling IFC Globally
Unique Identifiers (GUID). These GUIDs are standardized as 22-character
Base64 encoded strings, uniquely identifying elements in IFC models.

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library

# Import | Libraries
from django.db import models

# Import | Local Modules
from ...utils import validate_ifc_guid


# =============================================================================
# Variables
# =============================================================================

__all__ = ["IfcGloballyUniqueIdField", ]


# =============================================================================
# Classes
# =============================================================================

class IfcGloballyUniqueIdField(models.CharField):
    """
    IFC GUID Model Field Class
    ==========================

    A Django model field for storing IFC Globally Unique Identifiers (GUIDs).

    Enforces the format of 22-character Base64 encoded strings, ensuring
    they are unique within the database. Includes validation to check format
    correctness.

    Attributes:
        max_length (int): Maximum length of the field, set to 22 for IFC GUID.
        unique (bool): Ensures that all values in the database are unique.
        validators (list): List of validators applied to the field,
            specifically `validate_ifc_guid`.

    """

    def __init__(self, *args, **kwargs) -> None:
        """
        """
        kwargs['max_length'] = 22  # Ensure the length is always 22
        kwargs['unique'] = True  # Ensure uniqueness across database entries
        kwargs['validators'] = [validate_ifc_guid]
        super().__init__(*args, **kwargs)

    def from_db_value(
        self,
        value: str,
        expression,
        connection
    ) -> str:
        """
        Return the value directly from the database as is.
        """
        return value

    def to_python(self, value: str) -> str:
        """
        Ensure the value is a string and validate its format before
        converting it to a Python object.

        Parameters:
            value (str): The value from the database or user input.

        Returns:
            str: The validated and correctly formatted GUID string.
        """
        if isinstance(value, str):
            validate_ifc_guid(value)
        return value

    def get_prep_value(self, value: str) -> str:
        """
        Prepare the value for storage, ensuring it adheres to IFC GUID format.

        Parameters:
            value (str): The value to be stored in the database.

        Returns:
            str: The value prepared for database insertion, after validation.
        """
        validate_ifc_guid(value)
        return super().get_prep_value(value)
