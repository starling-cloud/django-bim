# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Role Enum Model Field Class
========================================

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library

# Import | Libraries
from typing import Any

from django.db import models

# Import | Local Modules
from ...enums.actor import IfcRoleEnum

# from django.utils.translation import gettext_lazy as _


# =============================================================================
# Variables
# =============================================================================


# =============================================================================
# Classes
# =============================================================================


class IfcRoleEnumField(models.CharField):
    """
    IFC Role Enum Model Field Class
    ===============================

    Custom Django field for storing role types based on the IfcRoleEnum.

    This field automatically uses IfcRoleEnum to provide choices for role
    types in IFC models, ensuring that the values adhere to the predefined
    roles specified by the IFC standards.

    Attributes:
        max_length (int): The maximum length of the string to store in the
            database, set to 50.
        choices (tuple): Dynamic choices pulled from IfcRoleEnum, provided
            at the class level.
        default (str): The default value for the field, set to "USERDEFINED"
            from IfcRoleEnum.
        verbose_name (str): Human-readable name for the field.
        help_text (str): Explanation of the field"s purpose and usage.
    """

    def __init__(
        self,
        *args,
        **kwargs,
    ) -> None:
        kwargs.setdefault("max_length", 50)
        kwargs.setdefault("choices", IfcRoleEnum.choices())
        kwargs.setdefault("default", IfcRoleEnum.USERDEFINED.name)
        super().__init__(*args, **kwargs)

    def deconstruct(self) -> tuple[Any, Any, Any, Any]:
        """
        Deconstructs the field to allow for custom field arguments to be
        correctly serialized by Django"s migration framework. This method
        ensures that the custom settings are preserved when generating
        migrations.

        """
        name, path, args, kwargs = super().deconstruct()
        # Ensure the migration includes the max_length
        kwargs["max_length"] = 50
        # Ensure the choices are set
        kwargs["choices"] = IfcRoleEnum.choices()
        # Ensure the default is set
        kwargs["default"] = IfcRoleEnum.USERDEFINED.name
        return name, path, args, kwargs


# =============================================================================
# Public Interface
# =============================================================================

__all__: list[str] = [
    "IfcRoleEnumField",
]
