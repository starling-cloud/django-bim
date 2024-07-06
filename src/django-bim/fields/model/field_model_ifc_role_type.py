# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Role Type Model Field Class
========================================

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library

# Import | Libraries
from django.db import models
# from django.utils.translation import gettext_lazy as _

# Import | Local Modules
from ...enums import IfcRoleEnum


# =============================================================================
# Variables
# =============================================================================

__all__ = ["IfcRoleTypeField", ]


# =============================================================================
# Classes
# =============================================================================

class IfcRoleTypeField(models.CharField):
    """
    FC Role Type Model Field Class
    ==============================

    Custom Django field for storing role types based on the IfcRoleEnum.

    This field automatically uses IfcRoleEnum to provide choices for role
    types in IFC models, ensuring that the values adhere to the predefined
    roles specified by the IFC standards.

    Attributes:
        max_length (int): The maximum length of the string to store in the
            database, set to 50.
        choices (tuple): Dynamic choices pulled from IfcRoleEnum, provided
            at the class level.
        default (str): The default value for the field, set to 'USERDEFINED'
            from IfcRoleEnum.
        verbose_name (str): Human-readable name for the field.
        help_text (str): Explanation of the field's purpose and usage.
    """

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 50)
        kwargs.setdefault('choices', IfcRoleEnum.choices())
        kwargs.setdefault('default', IfcRoleEnum.USERDEFINED.name)
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        """
        Deconstructs the field to allow for custom field arguments to be
        correctly serialized by Django's migration framework. This method
        ensures that the custom settings are preserved when generating
        migrations.

        """
        name, path, args, kwargs = super().deconstruct()
        # Ensure the migration includes the max_length
        kwargs['max_length'] = 50
        # Ensure the choices are set
        kwargs['choices'] = IfcRoleEnum.choices()
        # Ensure the default is set
        kwargs['default'] = IfcRoleEnum.USERDEFINED.name
        return name, path, args, kwargs
