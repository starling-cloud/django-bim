# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Timestamp Model Field Class
===================================


https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcmeasureresource/lexical/ifctimestamp.htm

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
import datetime

# Import | Libraries
from django.db import models
from django.utils.timezone import make_aware, get_default_timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Import | Local Modules


# =============================================================================
# Variables
# =============================================================================

__all__ = ["IfcTimestampField", ]


# =============================================================================
# Classes
# =============================================================================

class IfcTimestampField(models.TextField):
    """
    IFC Timestamp Model Field Class
    ===============================

    Custom Django field for storing IfcTimeStamp, which is the number of
    seconds since 00:00:00 Coordinated Universal Time (UTC), Thursday,
    1 January 1970.

    This field stores the time as an integer but interacts with Python's
    datetime objects, automatically handling conversion between these for
    ease of use within Django.

    """

    def from_db_value(self, value, expression, connection):
        """
        Convert an integer from the database to a datetime.datetime object.
        """
        if value is None:
            return value
        try:
            return make_aware(
                datetime.datetime.utcfromtimestamp(value),
                get_default_timezone()
            )
        # Handle overflow error which can happen with large timestamps
        except OverflowError:
            raise ValidationError(
                _("Timestamp value is out of range for datetime.")
            )

    def to_python(self, value):
        """
        Convert the value to a datetime.datetime object.
        """
        if isinstance(value, datetime.datetime):
            return value
        if value is None:
            return value
        try:
            return make_aware(
                datetime.datetime.utcfromtimestamp(int(value)),
                get_default_timezone()
            )
        except (ValueError, OverflowError):
            raise ValidationError(_("Invalid timestamp value."))

    def get_prep_value(self, value):
        """
        Convert the datetime.datetime object to an integer timestamp before
        saving to the database.
        """
        if isinstance(value, datetime.datetime):
            return int(value.timestamp())
        return value

    def value_to_string(self, obj):
        """
        Convert the datetime value to a string for serialization.
        """
        value = self.value_from_object(obj)
        return str(
            int(value.timestamp())
        ) if isinstance(value, datetime.datetime) else ''
