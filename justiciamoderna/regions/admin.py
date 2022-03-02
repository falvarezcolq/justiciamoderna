from django.contrib import admin

from .models import Region

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name','country',)

# admin.site.register(Region)



    # form = UserChangeForm
    # add_form = UserCreationForm
    # fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    # list_display = ["username", "name", "is_superuser"]
    # search_fields = ["name"]
