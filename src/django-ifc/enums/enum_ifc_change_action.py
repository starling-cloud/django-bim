# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Change Action Enum Class
=====================================


For more information, refer to:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcutilityresource/lexical/ifcchangeactionenum.htm

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

class IfcChangeActionEnum(Enum):
    """
    IFC Change Action Enum Class
    ============================

    Enumeration for IfcChangeActionEnum providing change types according to the
    IFC 2x3 standard.

    This enum represents the types of procedural changes that can be applied
    to project data, aiding in tracking modifications, additions, and
    deletions within IFC models.

    Enum Members:
    - NOCHANGE: Indicates no change was made.
    - MODIFIED: Indicates the object was modified.
    - ADDED: Indicates the object was added.
    - DELETED: Indicates the object was deleted.
    - NOTDEFINED: Used when the change action is not defined.
    """
    NOCHANGE = _('No Change')
    MODIFIED = _('Modified')
    ADDED = _('Added')
    DELETED = _('Deleted')
    NOTDEFINED = _('Not Defined')

    @classmethod
    def choices(cls):
        """
        Returns the choices for field choices in a Django model field,
        formatted as required by Django's field choices.

        Returns:
            tuple of tuples: Each tuple contains the enum member's name and
                its human-readable name, suitable for use in model field
                choices.
        """
        return tuple((item.name, item.value) for item in cls)
