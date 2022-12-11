from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Contact
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class DjangoResource(resources.ModelResource):
   class Meta:
      model = Contact
class DjangoAdmin(ImportExportModelAdmin):
   resource_class = DjangoResource

admin.site.register(Contact, DjangoAdmin)