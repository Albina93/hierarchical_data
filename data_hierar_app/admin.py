from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from . import models


admin.site.register(models.Movie, DraggableMPTTAdmin)
