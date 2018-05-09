from django.contrib import admin

from listing.models import Listing, Widget8, Widget9, Widget13, Widget14, Widget17


class ListingAdmin(admin.ModelAdmin):

    list_display = ('widget1', 'widget2', 'widget3', 'created_on', 'updated_on',)


class Widget8Admin(admin.ModelAdmin):

    list_display = ('widget_choice',)


class Widget9Admin(admin.ModelAdmin):

    list_display = ('widget_choice',)


class Widget13Admin(admin.ModelAdmin):

    list_display = ('widget_choice',)


class Widget14Admin(admin.ModelAdmin):

    list_display = ('widget_choice',)


class Widget17Admin(admin.ModelAdmin):

    list_display = ('widget_choice',)


admin.site.register(Listing, ListingAdmin)
admin.site.register(Widget8, Widget8Admin)
admin.site.register(Widget9, Widget9Admin)
admin.site.register(Widget13, Widget13Admin)
admin.site.register(Widget14, Widget14Admin)
admin.site.register(Widget17, Widget17Admin)
