from django.contrib import admin

from .models import Rol,RolPermission

@admin.register(Rol)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(RolPermission)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('rol','permission','state',)

# admin.site.register(Region)



    # form = UserChangeForm
    # add_form = UserCreationForm
    # fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    # list_display = ["username", "name", "is_superuser"]
    # search_fields = ["name"]
