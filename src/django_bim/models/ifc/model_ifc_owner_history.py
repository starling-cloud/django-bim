# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Owner History Model Class
======================================

This Django model tracks the ownership and modification history of IFC entities,
documenting who made changes, when these changes were made, and the nature of
these changes in line with the IFC standard.

For more information, refer to:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcutilityresource/lexical/ifcownerhistory.htm

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library

# Import | Libraries
from django.db import models
from django.utils.translation import gettext_lazy as _

# Import | Local Modules
from ...fields.model import (
    IfcTimestampField,
)
from ...enums import (
    IfcChangeActionEnum,
    IfcStateEnum,
)


# =============================================================================
# Variables
# =============================================================================


# =============================================================================
# Classes
# =============================================================================

class IfcOwnerHistoryModel(models.Model):
    """
    IFC Owner History Model Class
    =============================

    Model representing IFC Owner History.

    This model tracks modifications and ownership history related to IFC
    entities, capturing who made changes, when, and what kind of change was
    made, according to the IFC standard.

    Attributes:
        creation_user (ForeignKey): The user who initially created the entity.
        modification_user (ForeignKey): The user who last modified the entity.
        creation_date (IfcTimestampField): When the entity was created.
        last_modified_date (IfcTimestampField): When the entity was last
            modified.
        change_action (CharField): Type of change made (modified, added,
            deleted).
        state (CharField): State of the entity at the last modification.
        application (ForeignKey): Application used for the modification.

    """

    # Class | Model Fields
    # =========================================================================

    creation_user = models.ForeignKey(
        "IfcPersonAndOrganizationModel",
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = "created_ifc_entities",
        verbose_name = _("Creation User"),
        help_text = _("The user who initially created the entity.")
    )

    modification_user = models.ForeignKey(
        "IfcPersonAndOrganizationModel",
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = "modified_ifc_entities",
        verbose_name = _("Modification User"),
        help_text = _("The user who last modified the entity.")
    )

    creation_date = IfcTimestampField(
        auto_now_add = True,
        verbose_name = _("Creation Date"),
        help_text = _("The timestamp when the entity was created.")
    )

    last_modified_date = IfcTimestampField(
        auto_now = True,
        verbose_name = _("Last Modified Date"),
        help_text = _("The timestamp when the entity was last modified.")
    )

    change_action = models.CharField(
        max_length = 50,
        choices = IfcChangeActionEnum.choices(),
        default = IfcChangeActionEnum.NOTDEFINED.name,
        verbose_name = _("Change Action"),
        help_text = _(
            "The type of procedural action taken on the entity."
        )
    )

    state = models.CharField(
        max_length = 50,
        choices = IfcStateEnum.choices(),
        # default = IfcStateEnum.NOTDEFINED.name,
        verbose_name = _("State"),
        help_text = _(
            "The state of the entity at the last modification time."
        )
    )

    application = models.ForeignKey(
        "IfcApplicationModel",
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = "used_in_modifications",
        verbose_name = _("Application"),
        help_text = _(
            "The software application used to make the modification."
        )
    )

    # Class | Model Meta Class
    # =========================================================================

    class Meta:
        """
        Meta Class
        ----------

        """
        verbose_name = _("IFC Owner History")
        verbose_name_plural = _("IFC Owner Histories")
        indexes = [
            models.Index(
                fields = ["creation_user"],
                name = "idx_creation_user",
            ),
            models.Index(
                fields = ["modification_user"],
                name = "idx_modification_user",
            ),
        ]

    # Class | Model Methods
    # =========================================================================

    def __str__(self) -> str:
        """
        """
        creation_time = self.creation_date.strftime('%Y-%m-%d %H:%M:%S')
        return f"{self.creation_user.username if self.creation_user else 'Unknown User'} on {creation_time}"  # noqa E501


# =============================================================================
# Module Variables
# =============================================================================

__all__ = [
    "IfcOwnerHistoryModel",
]
