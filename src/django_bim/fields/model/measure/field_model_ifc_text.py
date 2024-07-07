# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Text Model Field Class
===================================


https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcmeasureresource/lexical/ifctext.htm

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

__all__ = ["IfcTextField", ]


# =============================================================================
# Classes
# =============================================================================

class IfcTextField(models.TextField):
    """
    IFC Text Model Field Class
    ==========================

    Custom field for IfcText, representing a textual description in IFC models.

    This field is tailored to meet the IFC standard requirements for textual
    data, such as descriptions, notes, or any other extensive textual
    information pertinent to IFC entities. It is based on Django"s TextField
    and ensures that data stored complies with the expected format for IFC
    text fields.

    Attributes:
        help_text (str): Guidance for input, specifying the field"s use
            according to IFC standards, displayed in admin or forms.

    """

    def __init__(self, *args, **kwargs):
        kwargs["help_text"] = kwargs.get(
            "help_text",
            _("Enter a textual description according to IFC standards.")
        )
        super().__init__(*args, **kwargs)

    def from_db_value(self, value: str, expression, connection) -> str:
        """
        Converts the value as returned by the database to a Python object.
        It is used when fetching the value of the field from the database.

        Parameters:
            value (str): The string value from the database.
            expression: Unused, included for compatibility with Django's
                signature.
            connection: Unused, included for compatibility with Django's
                signature.

        Returns:
            str: The value as a string, or None if the value is None.
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
            value (str): The value to be converted, either from the database
                or input.

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
        This method ensures the text is stored correctly in the database.

        Parameters:
            value (str): The string value to be prepared.

        Returns:
            str: The value formatted for database storage.
        """
        return super().get_prep_value(value)
