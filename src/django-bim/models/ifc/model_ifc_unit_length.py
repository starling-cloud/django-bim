class LengthUnit(IfcUnit):
    """
    Concrete model representing a specific type of IfcUnit for length measurements.

    Attributes:
        unit_name (CharField): The name of the length unit, e.g., meter, millimeter.
    """

    unit_name = models.CharField(
        max_length=100,
        verbose_name=_("Unit Name"),
        help_text=_("Name of the length unit, e.g., meter, millimeter.")
    )

    class Meta:
        verbose_name = _("Length Unit")
        verbose_name_plural = _("Length Units")

    def __str__(self):
        return f"{self.unit_name}"
