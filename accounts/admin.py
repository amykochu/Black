from django.contrib import admin
from accounts.models import User
from listing.models import Mandate


class MandateInline(admin.StackedInline):
    model = Mandate
    extra = 0


class UserAdmin(admin.ModelAdmin):
    inlines = [
        MandateInline,
    ]
    list_display = ('id', 'email', 'first_name', 'last_name', 'title', 'location', 'country', 'fund', 'mobile',
                    'land_line', )


admin.site.register(User, UserAdmin)
