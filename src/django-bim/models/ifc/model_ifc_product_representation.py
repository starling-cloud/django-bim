class IfcProductRepresentation(models.Model):
    # Simple representation for product representation details
    details = models.TextField(verbose_name=_("Representation Details"))