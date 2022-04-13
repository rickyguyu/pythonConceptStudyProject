from django.contrib import admin
from .models import Businessinfo
from .models import Userinfo

from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(Businessinfo)
class Userdata(ImportExportModelAdmin):
    pass