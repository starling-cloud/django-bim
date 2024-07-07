class IfcLine(IfcCurve):
    """
    Django model representing an IfcLine, which is a specific type of IfcCurve.

    Attributes:
        start_point (JSONField): Starting point of the line, stored as a JSON object.
        end_point (JSONField): Ending point of the line, stored as a JSON object.
    """

    start_point = models.JSONField(
        verbose_name=_("Start Point"),
        help_text=_("JSON representation of the start point coordinates.")
    )
    end_point = models.JSONField(
        verbose_name=_("End Point"),
        help_text=_("JSON representation of the end point coordinates.")
    )

    def __str__(self):
        return f"Line from {self.start_point} to {self.end_point}"
