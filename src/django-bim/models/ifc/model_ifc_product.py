https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifckernel/lexical/ifcproduct.htm

class IfcProduct(IfcObjectDefinition):
    """
    Django model representing an IfcProduct as defined in the IFC 2x3 standard.

    IfcProduct is the base class for all physical elements that have a physical manifestation
    and can be spatially located and oriented.

    Attributes:
        object_placement (ForeignKey): Specifies the placement of the product in space.
        representation (ForeignKey): Links to the geometric and/or topological representation of the product.
    """

    object_placement = models.ForeignKey(
        IfcObjectPlacement,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Object Placement"),
        help_text=_("Specifies the placement of the product in space.")
    )

    representation = models.ForeignKey(
        IfcProductRepresentation,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Representation"),
        help_text=_("Links to the geometric and/or topological representation of the product.")
    )

    class Meta:
        verbose_name = _("IfcProduct")
        verbose_name_plural = _("IfcProducts")

    def __str__(self):
        return f"{self.name} - Placement: {self.object_placement}, Representation: {self.representation}"


# =============================================================================
# Module Variables
# =============================================================================

