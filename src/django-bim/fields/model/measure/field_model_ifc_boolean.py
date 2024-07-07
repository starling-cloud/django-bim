https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcmeasureresource/lexical/ifcboolean.htm

from django.db import models
from django.utils.translation import gettext_lazy as _

class IfcBooleanModelField(models.IntegerField):
    """
    Custom Django field to represent the IFC boolean type, which includes True, False, and Unknown states.
    
    - 1 represents True
    - 0 represents False
    - -1 represents Unknown
    """
    description = _("A boolean field for IFC that supports True, False, and Unknown states.")

    def __init__(self, *args, **kwargs):
        kwargs["choices"] = (
            (1, _("True")),
            (0, _("False")),
            (-1, _("Unknown"))
        )
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return {
            1: True,
            0: False,
            -1: None
        }.get(value, None)

    def to_python(self, value):
        if value in (True, 1):
            return True
        elif value in (False, 0):
            return False
        elif value in (None, -1):
            return None
        raise ValueError("Invalid value for IfcBooleanField")

    def get_prep_value(self, value):
        """
        Convert the Python value into format that's saveable to the database.
        """
        if value is True:
            return 1
        elif value is False:
            return 0
        elif value is None:
            return -1
        raise ValueError("Invalid value for IfcBooleanField")
