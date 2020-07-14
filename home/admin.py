from django.contrib import admin
from .models import Contact

# Register your models here.
# admin.site.register(Contact)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
  fields = (('firstname', 'lastname'),'email', 'address', ('city','state'), 'msg','rating')
  list_display = ('firstname', 'lastname', 'city','state')
  list_filter = ('city', 'state')
  ordering = ('firstname',)
  search_fields = ('firstname', 'lastname','city','state')
