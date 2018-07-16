from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.contrib.auth import get_user_model


from listing.models import (Opportunity, Mandate, InvestmentOffered, ValuationFundTicket, Yield, Class,
                            SeriesStage, InvestorSpecial, EstPayback, Offer, Financial, Country, Geography,
                            SubSector, Sector, CompanyPurchaseMinMax, Category, FundSize)
from listing.forms import MandateChangeListForm


User = get_user_model()


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


class MandateChangeList(ChangeList):

    def __init__(self, request, model, list_display, list_display_links,
                 list_filter, date_hierarchy, search_fields, list_select_related,
                 list_per_page, list_max_show_all, list_editable, model_admin):
        super(MandateChangeList, self).__init__(request, model, list_display, list_display_links,
                                                    list_filter, date_hierarchy, search_fields, list_select_related,
                                                    list_per_page, list_max_show_all, list_editable, model_admin)

        # these need to be defined here, and not in MandateAdmin
        self.list_display = ['action_checkbox', 'email', 'first_name', 'last_name', 'title', 'location',
                             'user_country',
                             'fund', 'mobile', 'land_line', 'category',
                             'investment_sought', 'fund_description',
                             'fund_size', 'size_ticket_total', 'percentage_company_min', 'percentage_company_max',
                             'display_geography', 'country', 'display_sector', 'sub_sector', 'yield_select',
                             'growth_expectation_year1', 'growth_expectation_year2', 'growth_expectation_year3',
                             'class_select', 'series_stage', 'investor_required', 'fund_size_select',
                             'created_on', 'updated_on']
        # self.list_display_links = ['user']
        self.list_editable = ['email', 'first_name', 'last_name', 'title', 'location', 'user_country', 'fund', 'mobile',
                              'land_line', 'category', 'investment_sought',
                              'fund_description', 'fund_size', 'size_ticket_total', 'percentage_company_min',
                              'percentage_company_max', 'country', 'sub_sector', 'yield_select',
                              'growth_expectation_year1', 'growth_expectation_year2', 'growth_expectation_year3',
                              'class_select', 'series_stage', 'investor_required', 'fund_size_select']


class MandateAdmin(admin.ModelAdmin):
    def get_changelist(self, request, **kwargs):
        return MandateChangeList

    def get_changelist_form(self, request, **kwargs):
        return MandateChangeListForm


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

