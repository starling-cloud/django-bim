# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Label Model Field Class
====================================


https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcmeasureresource/lexical/ifclabel.htmfrom django.db import models

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library

# Import | Libraries
from django.db import models
from django.utils.translation import gettext_lazy as _

# Import | Local Modules


# =============================================================================
# Variables
# =============================================================================

__all__ = ["IfcLabelField", ]


# =============================================================================
# Classes
# =============================================================================

class IfcLabelField(models.CharField):
    """
    IFC Label Model Field Class
    ===========================

    Custom field for IfcLabel, representing a label, identifier, or name in
    IFC models.

    This custom field is based on Django's CharField and is designed to ensure
    compliance with the IFC standard for labels, typically used for short
    texts like names, titles, or other identifiers. It defaults to a maximum
    length of 255 characters unless specified otherwise.

    Attributes:
        max_length (int): Maximum length of the field.
        help_text (str): Description of the field usage, provided to guide
        users in admin or forms.

    """

    def __init__(self, *args, **kwargs) -> None:
        """
        """
        # Default max length for IfcLabel
        kwargs["max_length"] = kwargs.get("max_length", 255)
        kwargs["help_text"] = kwargs.get(
            "help_text",
            _("Enter a label or identifier according to IFC standards.")
        )
        super().__init__(*args, **kwargs)

    def from_db_value(self, value: str, expression, connection) -> str:
        """
        Converts the value as returned by the database to a Python object.
        It is used when fetching the value of the field from the database.

        Parameters:
            value (str): The string value from the database.
            expression: The expression (unused here, included for method
                signature compliance).
            connection: The database connection (unused here, included for
                method signature compliance).

        Returns:
            str: The string value or None if the value is None.
        """
        if value is None:
            return value
        return str(value)

    def to_python(self, value: str) -> str:
        """
        Converts the value into the correct Python object. It acts as a
        deserializer for the Django field system and is called during form
        clean and data loading.

        Parameters:
            value (str): The string value from the database or input.

        Returns:
            str: The value as a string, ensuring it matches the expected
                data type.
        """
        if isinstance(value, str) or value is None:
            return value
        return str(value)

    def get_prep_value(self, value: str) -> str:
        """
        Prepares the value before saving it into the database.
        This method ensures the label is stored correctly in the database.

        Parameters:
            value (str): The string value to be prepared.

        Returns:
            str: The value formatted as a string ready for database insertion.
        """
        return super().get_prep_value(value)
