from django import forms

from listing.models import (Opportunity, Mandate, Geography, Sector, ValuationFundTicket, Yield, InvestmentOffered,
                            Class, SeriesStage)


class OpportunityForm(forms.ModelForm):
    """ Form to upload Opportunity data """

    geography = forms.ModelMultipleChoiceField(queryset=Geography.objects.all())
    sector = forms.ModelMultipleChoiceField(queryset=Sector.objects.all())
    required_css_class = 'required'

    class Meta:
        model = Opportunity
        fields = ('company_description', 'opportunity_created', 'selling_by', 'competitors', 'valuation',
                  'valuation_text', 'amount_invested', 'ownership_structure', 'ebitda', 'break_even_year',
                  'est_payback', 'size_ticket_total', 'geography', 'country', 'sector', 'sub_sector', 'yield_select',
                  'return_estimate', 'growth_expectation_year1', 'growth_expectation_year2', 'growth_expectation_year3',
                  'class_select', 'series_stage', 'investor_required', 'amount_lead_partner', 'amount_other_partner',
                  'amount_weraise', 'investment_offered', 'offer', 'special_situation', 'financials', 'estimated_irr',
                  'exit_timing', 'use_of_funds', 'deadline_commitment', 'deadline_legal', 'proposed_process',
                  'proposed_exit', 'financial_statements', 'financial_model', 'investor_deck', 'company_bio',
                  'ceo_bio',)
        # exclude = ('revenue_json_data', )


class MandateForm(forms.ModelForm):
    """ Form for Investor Mandate upload """

    geography = forms.ModelMultipleChoiceField(queryset=Geography.objects.all())
    sector = forms.ModelMultipleChoiceField(queryset=Sector.objects.all())
    required_css_class = 'required'

    class Meta:
        model = Mandate
        fields = ('investment_sought', 'fund_size', 'size_ticket_total', 'percentage_company_min',
                  'percentage_company_max', 'geography', 'country', 'sector', 'sub_sector', 'yield_select',
                  'growth_expectation_year1',
                  'growth_expectation_year2', 'growth_expectation_year3', 'class_select', 'series_stage',
                  'investor_required',)


class OpportunitySearchForm(forms.ModelForm):
    """ Form for search """

    size_ticket_total = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple, queryset=ValuationFundTicket.objects.all(), required=False)
    sector = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple, queryset=Sector.objects.all(), required=False)
    yield_select = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple, queryset=Yield.objects.all(), required=False)
    investment_offered = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple, queryset=InvestmentOffered.objects.all(), required=False)
    series_stage = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple, queryset=SeriesStage.objects.all(), required=False)
    class_select = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple, queryset=Class.objects.all(), required=False)

    class Meta:
        model = Opportunity
        fields = ('size_ticket_total', 'sector', 'yield_select',
                  'investment_offered', 'series_stage', 'class_select')

    # def __init__(self, *args, **kwargs):
    #     super(OpportunitySearchForm, self).__init__(*args, **kwargs)
    #     self.fields['size_ticket_total'].required = False
    #     self.fields['sub_sector'].required = False
    #     self.fields['yield_select'].required = False
    #     self.fields['investment_offered'].required = False
    #     self.fields['series_stage'].required = False
    #     self.fields['class_select'].required = False

