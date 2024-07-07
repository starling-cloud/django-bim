https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcActorSelect.htm

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

class IfcActorSelectField(models.Field):
    description = _(
        "A field that can refer to an IfcOrganization, IfcPerson, or IfcPersonAndOrganization"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object_id_field = 'object_id'
        self.content_type_field = 'content_type'

    def contribute_to_class(self, cls, name, private_only=False, **kwargs):
        self.name = name
        self.model = cls
        ct_field = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={
            'model__in': ('ifcperson', 'ifcorganization', 'ifcpersonandorganization')
        })
        fk_field = models.PositiveIntegerField()
        cls.add_to_class(self.content_type_field, ct_field)
        cls.add_to_class(self.object_id_field, fk_field)
        actor = GenericForeignKey(self.content_type_field, self.object_id_field)
        cls.add_to_class(name, actor)

        super().contribute_to_class(cls, name, private_only, **kwargs)

    def get_internal_type(self):
        return 'IfcActorSelectField'
