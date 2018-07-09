from django.contrib import admin

from listing.models import (Opportunity, Mandate, InvestmentOffered, ValuationFundTicket, Yield, Class,
                            SeriesStage, InvestorSpecial, EstPayback, Offer, Financial, Country, Geography,
                            SubSector, Sector, CompanyPurchaseMinMax, Category, FundSize)


class MandateAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'display_investment_sought', 'display_size_ticket_total',
                    'display_geography', 'display_country', 'display_sector',
                    'display_sub_sector', 'display_series_stage',  'display_class_select', 'display_yield_select',
                    'growth_expectation_year1', 'growth_expectation_year2', 'growth_expectation_year3',
                    'percentage_company_min', 'percentage_company_max', 'investor_required',
                    'created_on', 'updated_on')


class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_description',  'valuation', 'valuation_text', 'display_sector', 'display_sub_sector',
                    'display_geography', 'display_country', 'ownership_structure', 'opportunity_created',
                    'selling_by', 'competitors', 'display_size_ticket_total',
                    'use_of_funds', 'display_investment_offered', 'display_class_select', 'display_series_stage',
                    'display_offer', 'special_situation', 'proposed_process', 'investor_required', 'amount_lead_partner',
                    'amount_other_partner', 'amount_weraise', 'deadline_commitment', 'deadline_legal',
                    'amount_invested', 'display_est_payback', 'estimated_irr', 'break_even_year', 'yield_select',
                    'proposed_exit', 'exit_timing', 'ebitda', 'financials', 'financial_statements', 'financial_model',
                    'investor_deck', 'display_company_bio', 'display_ceo_bio',
                    # 'return_estimate', 'growth_expectation_year1', 'growth_expectation_year2',
                    # 'growth_expectation_year3',
                    'created_on', 'updated_on')


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
admin.site.register(Category)
admin.site.register(FundSize)

