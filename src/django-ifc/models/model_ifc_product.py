https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifckernel/lexical/ifcproduct.htm

from django.db import models

class IfcProduct(models.Model):
    # Attributes
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    object_placement = models.JSONField(blank=True, null=True, help_text="Spatial structure defining the object's placement in the project.")
    representation = models.JSONField(blank=True, null=True, help_text="Physical or geometric representation of the product.")
    
    # Relationships
    project = models.ForeignKey('IfcProject', on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    owner_history = models.ForeignKey('IfcOwnerHistory', on_delete=models.SET_NULL, null=True, blank=True, help_text="Information about the creation or modification of the product.")

    def __str__(self):
        return self.name or "Unnamed Product"

