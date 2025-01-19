# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC GUID Validation Function
=====================================

This module contains a validation function for ensuring that a given string
meets the IFC Globally Unique Identifier (GUID) specifications, as required by
the  Industry Foundation Classes (IFC) standards. The IFC GUID is typically
a 22-character Base64 encoded string, uniquely identifying IFC entities.

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
# import uuid
import re  # Used for regular expression matching

# Import | Libraries
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Import | Local Modules


# =============================================================================
# Variables
# =============================================================================

__all__: list[str] = [
    "validate_ifc_guid",
]


# =============================================================================
# Functions
# =============================================================================


def validate_ifc_guid(value) -> None:
    """
    IFC GUID Validation Function
    ============================

    Validates that the given value conforms to the 22-character Base64
    requirement of IfcGloballyUniqueId.

    Parameters:
        value (str): The string to validate as an IFC Globally Unique
            Identifier.

    Raises:
        ValidationError: If the string does not conform to the expected format.
    """

    # Define the regex pattern for a Base64 encoded string of 22 characters
    pattern = r"^[A-Za-z0-9+/]{22}$"

    # Check if the provided value matches the pattern
    if not isinstance(value, str) or not re.match(
        pattern=pattern,
        string=value,
    ):
        raise ValidationError(
            message=_(
                message="'%(value)s' is not a valid 22-character Base64 encoded string."
            ),  # noqa E501
            params={"value": value},
            code="invalid",  # Including an error code for programmatic handling
        )
