# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Address Type Enum Class
====================================


For more information, refer to:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcactorresource/lexical/ifcaddresstypeenum.htm

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

class IfcAddressTypeEnum(Enum):
    """
    IFC Address Type Enum Class
    ===========================

    Enumeration for IfcAddressTypeEnum providing address types according to
    the IFC 2x3 standard.

    Each member of this enumeration represents a specific type of address
    that may be associated with various entities involved in a building
    project.

    Enum Members:
    - OFFICE: An address used for office purposes.
    - SITE: An address specifying a construction site.
    - HOME: The personal home address of an individual.
    - DISTRIBUTIONPOINT: An address used for distribution.
    - USERDEFINED: User-defined type of address not covered by other
        categories.
    - NOTDEFINED: For addresses that do not fit any of the predefined types.
    """

    OFFICE = _('Office')
    SITE = _('Site')
    HOME = _('Home')
    DISTRIBUTIONPOINT = _('Distribution Point')
    USERDEFINED = _('User Defined')
    NOTDEFINED = _('Not Defined')

    @classmethod
    def choices(cls):
        """
        Returns the choices for field choices in a Django model field,
        formatted as required by Django's field choices.

        Returns:
            tuple of tuples: Each tuple contains the enum member's value and
                its human-readable name.
        """

        return tuple((item.name, item.value) for item in cls)
