# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC State Enum Class
============================



For more information, refer to:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcutilityresource/lexical/ifcstateenum.htm

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
from enum import Enum
# from typing import Any, Dict, List

# Import | Libraries
from django.utils.translation import gettext_lazy as _

# Import | Local Modules


# =============================================================================
# Classes
# =============================================================================

class IfcStateEnum(Enum):
    """
    IFC State Enum Class
    ===================

    Enumeration for IfcStateEnum providing state types according to the
    IFC 2x3 standard.

    This enum represents different states an object in a building construction
    project can have, helping to manage object status within the project's
    lifecycle.

    Enum Members:
    - READWRITE: The object is available for reading and writing.
    - READONLY: The object is only available for reading.
    - LOCKED: The object is locked and cannot be modified.
    - READWRITELOCKED: The object is locked but can be read or written to by
        the locking user.
    - READONLYLOCKED: The object is locked and can only be read by the
        locking user.
    """
    READWRITE = _('Read-Write')
    READONLY = _('Read-Only')
    LOCKED = _('Locked')
    READWRITELOCKED = _('Read-Write Locked')
    READONLYLOCKED = _('Read-Only Locked')

    @classmethod
    def choices(cls):
        """
        Returns the choices for field choices in a Django model field,
        formatted as required by Django's field choices.

        Returns:
            tuple of tuples: Each tuple contains the enum member's name and its
                human-readable name, suitable for use in model field choices.
        """
        return tuple((item.name, item.value) for item in cls)