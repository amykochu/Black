from django.contrib import admin
from accounts.models import User
from listing.models import Mandate


class MandateInline(admin.StackedInline):
    model = Mandate
    extra = 0

    def has_add_permission(self, request):
        return False


class UserAdmin(admin.ModelAdmin):
    inlines = [
        MandateInline,
    ]
    list_display = ('id', 'email', 'first_name', 'last_name', 'title', 'location', 'country', 'fund', 'mobile_code',
                    'mobile', 'land_line_code', 'land_line', 'user_type', 'is_active')
    exclude = ('password', 'last_login', 'groups', 'user_permissions')


admin.site.register(User, UserAdmin)
