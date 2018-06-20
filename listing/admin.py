from django.contrib import admin

from listing.models import (Opportunity, Mandate, InvestmentOffered, ValuationFundTicket, Yield, Class,
                            SeriesStage, InvestorSpecial, EstPayback, Offer, Financial, Country, Geography,
                            SubSector, Sector, CompanyPurchaseMinMax)


class MandateAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'percentage_company_min', 'percentage_company_max', 'display_investment_sought',
                    'display_size_ticket_total', 'display_yield_select', 'growth_expectation_year1', 'display_country',
                    'growth_expectation_year2', 'growth_expectation_year3', 'display_sub_sector',
                    'investor_required', 'display_class_select', 'display_series_stage',
                    'created_on', 'updated_on')


class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_description', 'opportunity_created', 'selling_by', 'competitors', 'valuation',
                    'valuation_text', 'amount_invested', 'ownership_structure', 'ebitda', 'break_even_year',
                    'display_est_payback', 'display_size_ticket_total', 'display_country', 'display_sub_sector',
                    'yield_select', 'return_estimate', 'growth_expectation_year1', 'growth_expectation_year2',
                    'growth_expectation_year3', 'display_class_select', 'display_series_stage', 'investor_required',
                    'amount_lead_partner', 'amount_other_partner', 'amount_weraise', 'display_investment_offered',
                    'display_offer', 'special_situation', 'financials', 'estimated_irr',
                    'exit_timing', 'use_of_funds', 'deadline_commitment', 'deadline_legal', 'proposed_process',
                    'proposed_exit', 'financial_statements', 'financial_model', 'investor_deck', 'company_bio',
                    'ceo_bio', 'created_on', 'updated_on')


admin.site.register(Mandate, MandateAdmin)
admin.site.register(Opportunity, OpportunityAdmin)
admin.site.register(InvestmentOffered)
admin.site.register(ValuationFundTicket)
admin.site.register(Yield)
admin.site.register(Class)
admin.site.register(SeriesStage)
admin.site.register(InvestorSpecial)
admin.site.register(EstPayback)
admin.site.register(Offer)
admin.site.register(Financial)
admin.site.register(Country)
admin.site.register(Geography)
admin.site.register(Sector)
admin.site.register(SubSector)
admin.site.register(CompanyPurchaseMinMax)
# admin.site.register(Widget8, Widget8Admin)

