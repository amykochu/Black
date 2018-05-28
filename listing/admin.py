from django.contrib import admin

from listing.models import (Opportunity, Mandate, InvestmentOffered, ValuationFundTicket, Yield, Class,
                            SeriesStage, InvestorSpecial, EstPayback, Offer, Financial)


# class ListingAdmin(admin.ModelAdmin):
#
#     list_display = ('widget1', 'widget2', 'widget3', 'created_on', 'updated_on',)

admin.site.register(Mandate)
admin.site.register(Opportunity)
admin.site.register(InvestmentOffered)
admin.site.register(ValuationFundTicket)
admin.site.register(Yield)
admin.site.register(Class)
admin.site.register(SeriesStage)
admin.site.register(InvestorSpecial)
admin.site.register(EstPayback)
admin.site.register(Offer)
admin.site.register(Financial)
# admin.site.register(Year)

# admin.site.register(Widget8, Widget8Admin)

