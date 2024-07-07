# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Django BIM Config Class
===============================


This module defines the Django application configuration for the Django IFC
application, which is used to manage building data based on Industry
Foundation Classes (IFC). The AppConfig subclass sets several configurations
that control various aspects of the application's behavior in a Django project.

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
# from typing import Dict, List, Union

# Import | Libraries
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

# Import | Local Modules


# =============================================================================
# Classes
# =============================================================================

class DjangoBimConfig(AppConfig):
    """
    Django BIM Config Class
    ======================

    Django AppConfig for managing the Django IFC application.

    Attributes:
        name (str): The full Python path to the Django IFC application.
        label (str): A short, unique name for the application.
        verbose_name (str): A human-readable name for the application.
        default_auto_field (str): The implicit primary key type to add to
            models within this app.

    Note:
        It's essential to use unique labels if you have multiple instances
        of an application included in your project, especially when they
        belong to different versions or configurations.

    """

    # Full Python path to the application
    name = "django-bim"

    # Short name for the application, used in relation naming
    label = "django-bim"

    # Human-readable name for the application
    verbose_name = _("Django BIM")

    # Specifies the type of primary key to use by default for models in
    # this application
    default_auto_field = "django.db.models.BigAutoField"
