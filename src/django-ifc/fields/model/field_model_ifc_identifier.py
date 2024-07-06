# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Identifier Model Field Class
========================================

https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcmeasureresource/lexical/ifcidentifier.htm


"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library

# Import | Libraries
from django.db import models
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _

# Import | Local Modules


# =============================================================================
# Variables
# =============================================================================

__all__ = ["IfcIdentifierField", ]


# =============================================================================
# Classes
# =============================================================================

class IfcIdentifierField(models.CharField):
    """
    IFC Identifier Model Field Class
    ===============================

    Custom field for IfcIdentifier, representing a unique identifier in
    IFC models.

    This field is tailored to store identifiers that are used within the IFC
    framework to uniquely identify objects. It is based on Django's CharField
    and can be customized to include specific validation rules if IFC standards
    for identifiers include any such requirements.

    """

    def __init__(self, *args, **kwargs):
        """
        """
        # Default max length for IfcIdentifier
        kwargs['max_length'] = kwargs.get('max_length', 255)
        super().__init__(*args, **kwargs)

    def from_db_value(self, value: str, expression, connection) -> str:
        """
        Returns the value directly from the database as is.
        """
        return value

    def to_python(self, value: str) -> str:
        """
        Converts the value into the correct Python object. It acts as a
        deserializer for the Django field system and is called during form
        clean and data loading.

        Parameters:
            value (str): The value from the database or user input.

        Returns:
            str: The validated and correctly formatted identifier string.
        """
        if isinstance(value, str) or value is None:
            return value
        return str(value)

    def get_prep_value(self, value: str) -> str:
        """
        Prepares the value before saving it into the database.

        Parameters:
            value (str): The string value to be prepared.

        Returns:
            str: The value formatted for database storage.
        """
        return super().get_prep_value(value)

    def validate(self, value: str, model_instance):
        """
        Adds any additional validation for IfcIdentifier to ensure it meets
        IFC's standard requirements for format, uniqueness, etc., if
        applicable.

        Parameters:
            value (str): The identifier to validate.
            model_instance: The instance of the model where the field is
                defined.

        Raises:
            ValidationError: If the identifier does not meet the required
                standards.

        """
        super().validate(value, model_instance)
        # Implement any specific IFC identifier validations here
