from django.db import models
from django.utils.translation import gettext_lazy as _

class IfcCurve(models.Model):
    """
    Abstract Django model representing an IfcCurve as defined in the IFC 2x3 standard.
    
    IfcCurve is the abstract supertype for all curve entities within the IFC schema. This model
    provides a common interface for all derived curve types, encapsulating essential properties
    and behaviors of curve geometry.

    Attributes:
        curve_name (CharField): Optional name or description of the curve.
    """

    curve_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Curve Name"),
        help_text=_("Optional name or description of the curve.")
    )

    class Meta:
        abstract = True  # This model will not be created in the database
        verbose_name = _("IFC Curve")
        verbose_name_plural = _("IFC Curves")

    def __str__(self):
        return self.curve_name if self.curve_name else super().__str__()

