from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from justiciamoderna.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()

from justiciamoderna.users.models import UserPermission,Lawyer,Degree,Profile,ProfilePicture

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    # fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets

    fieldsets = (
        (_('Crendentials'), {'fields': ('username', 'password')}),

        (_('Personal info'), {'fields': (
                                         'first_name',
                                         'last_name',
                                         )}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser',
                       # , 'groups', 'user_permissions'
                       # 'active'
                       'reviewed_by_admin',
                       ),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined',)}),

        # (_('Documents'), {'fields': ('', 'date_joined',)}),

        # (_('Audit info'), {'fields': ("created_at", "updated_at", "deleted_at",
        #                               "created_by", "updated_by", "deleted_by")}),
    )

    readonly_fields = [ 'last_login', 'date_joined', ]
    search_fields = ["name"]
    list_filter = ['reviewed_by_admin','rol']

    list_display = ["username",
                    "name",
                    "need_update_profile",
                    "is_superuser",
                    "reviewed_by_admin",
                    "rol",
                    "view_lawyer_degrees_link",
                    "view_profile_picture_link",
                    "date_joined",]

    def view_lawyer_degrees_link(self,obj):
        count = obj.degrees.count()
        if count == 0 :
            return count
        url = (
            reverse("admin:users_degree_changelist")
            + "?"
            + urlencode({"user__id": f"{obj.id}"})
        )
        return format_html('<a href="{}"> {} {}</a>', url, count,_("Degrees"))

    view_lawyer_degrees_link.short_description = _("Degrees")

    def view_profile_picture_link(self,obj):
        count = obj.profilepictures.count()

        if count == 0 :
            return count
        url = (
            reverse("admin:users_profilepicture_changelist")
            + "?"
            + urlencode({"user__id": f"{obj.id}"})
        )
        return format_html('<a href="{}"> {} {}</a>', url, count,_("Pictures"))

    view_profile_picture_link.short_description = _("Profile picture")

admin.site.site_header = _("Administrator Justicia Moderna")

admin.site.register(UserPermission)

# admin.site.register(Lawyer)
@admin.register(Lawyer)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('user','matricula','view_lawyer_degrees_link')

    def view_lawyer_degrees_link(self,obj):
        count = obj.user.degrees.count()
        if count == 0 :
            return count
        url = (
            reverse("admin:users_degree_changelist")
            + "?"
            + urlencode({"user__id": f"{obj.user.id}"})
        )
        return format_html('<a href="{}">{} {}</a>', url, count,_("Degrees"))

        # return count

    view_lawyer_degrees_link.short_description = _("Degrees")



admin.site.register(Degree)


@admin.register(ProfilePicture)
class RegionAdmin(admin.ModelAdmin):
    fieldsets = (
        # (_('User'), {'fields': ('user')}),
        (_('Images'), {'fields': ('img_l', 'img_m', 'thumbnail')}),
    )
    list_display = ('user','img_l', 'img_m','thumbnail','is_current_profile_picture')



admin.site.register(Profile)


