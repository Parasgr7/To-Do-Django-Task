from django.contrib import admin
from registration.models import  Registration
from registration.actions import export_as_csv_action

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    actions = [export_as_csv_action("CSV Export", fields=['title', 'description','status'])]
    list_display = ('title', 'description', 'time', 'status','created_date','modified_date')
    list_filter = ('status','time','created_date','modified_date',)
    search_fields = ('title', 'description',)



admin.site.register(Registration,RegisterAdmin)