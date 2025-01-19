# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""

===================================

https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcActorSelect.htm


"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
from typing import Literal

# Import | Libraries
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

# Import | Local Modules


# =============================================================================
# Classes
# =============================================================================


class IfcActorSelectField(models.Field):
    """
    ...
    """

    description: str = _(
        message="A field that can refer to an IfcOrganization, IfcPerson, or IfcPersonAndOrganization"
    )

    def __init__(self, *args, **kwargs) -> None:
        """
        ...
        """
        super().__init__(*args, **kwargs)
        self.object_id_field = "object_id"
        self.content_type_field = "content_type"

    def contribute_to_class(
        self,
        cls,
        name,
        private_only=False,
        **kwarg,
    ) -> None:
        """
        ...
        """
        self.name = name
        self.model = cls
        ct_field = models.ForeignKey(
            ContentType,
            on_delete=models.CASCADE,
            limit_choices_to={
                "model__in": (
                    "ifcperson",
                    "ifcorganization",
                    "ifcpersonandorganization",
                ),
            },
        )
        fk_field = models.PositiveIntegerField()
        cls.add_to_class(self.content_type_field, ct_field)
        cls.add_to_class(self.object_id_field, fk_field)
        actor = GenericForeignKey(
            ct_field=self.content_type_field, fk_field=self.object_id_field
        )
        cls.add_to_class(name, actor)

        super().contribute_to_class(
            cls=cls,
            name=name,
            private_only=private_only,
            **kwargs,
        )

    def get_internal_type(self) -> Literal["IfcActorSelectField"]:
        """
        ...
        """
        return "IfcActorSelectField"


# =============================================================================
# Export
# =============================================================================

__all__: list[str] = [
    "IfcActorSelectField",
]
