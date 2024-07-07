# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC ... Model Class
===================================

For more information, refer to:

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library

# Import | Libraries
from django.db import models
from django.utils.translation import gettext_lazy as _

# Import | Local Modules
from ...fields.model import (
    IfcLabelField,
    IfcRoleTypeField,
    IfcTextField,
)


# =============================================================================
# Classes
# =============================================================================

class IfcProductRepresentation(models.Model):
    # Simple representation for product representation details
    details = models.TextField(verbose_name=_("Representation Details"))


# =============================================================================
# Module Variables
# =============================================================================

__all__ = [
    "IfcActorRoleModel",
]
