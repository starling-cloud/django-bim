from django.db import models


class Building(models.Model):
    """
    """
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class Building(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='buildings')
    name = models.CharField(max_length=255)
    location_description = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.name


class IfcBuilding(models.Model):
    # Core Attributes
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    # Relational Attributes
    object_placement = models.JSONField(blank=True, null=True, help_text="Spatial structure of the building.")
    representation = models.JSONField(blank=True, null=True, help_text="Representation of the building in terms of geometry or other parameters.")

    # Specific Attributes
    elevation_of_ref_height = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, help_text="Elevation at reference height above sea level.")
    elevation_of_terrain = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, help_text="Elevation of the natural terrain around the building's perimeter at reference height.")
    building_address = models.JSONField(blank=True, null=True, help_text="Address of the building.")

    # Relationships (For simplicity, assuming relationships are managed as JSON. Adjust according to your application's needs.)
    building_elements = models.JSONField(blank=True, null=True, help_text="Elements that form part of the building.")
    project = models.ForeignKey('IfcProject', on_delete=models.CASCADE, related_name='buildings', blank=True, null=True)

    def __str__(self):
        return self.name or "Unnamed Building"
