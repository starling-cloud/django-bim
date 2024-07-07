class IfcCartesianPoint(IfcRepresentationItem):
    """
    Model representing an IfcCartesianPoint, which defines a point in 2D or
    3D space by its coordinates.

    """

    x = models.FloatField(verbose_name=_("X Coordinate"))
    y = models.FloatField(verbose_name=_("Y Coordinate"))
    z = models.FloatField(blank=True, null=True, verbose_name=_("Z Coordinate"), help_text=_("Z coordinate is optional for 3D points."))


    # Class | Model Meta Class
    # =========================================================================

    # Class | Model Methods
    # =========================================================================

    def __str__(self) -> str:
        """
        """
        if self.z is not None:
            return f"Point({self.x}, {self.y}, {self.z})"
        return f"Point({self.x}, {self.y})"


# =============================================================================
# Module Variables
# =============================================================================
