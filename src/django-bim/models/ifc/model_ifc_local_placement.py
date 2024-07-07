class IfcLocalPlacement(IfcObjectPlacement):
    """
    Model representing an IfcLocalPlacement, which defines an object placement
    relative to the placement of another object.

    Attributes:
        relative_placement (ForeignKey): The object to which this placement is relative.
    """

    relative_placement = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='related_placements',
        verbose_name=_("Relative Placement"),
        help_text=_("The object placement to which this placement is relative.")
    )

    def __str__(self):
        relative_info = f", Relative to: {self.relative_placement.placement_id}" if self.relative_placement else ""
        return f"{super().__str__()} {relative_info}"
