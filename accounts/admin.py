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
    list_display = ('id', 'email', 'first_name', 'last_name', 'title', 'location', 'country', 'fund', 'mobile',
                    'land_line', )
    exclude = ('password', 'last_login', 'groups', 'user_permissions')

admin.site.register(User, UserAdmin)
