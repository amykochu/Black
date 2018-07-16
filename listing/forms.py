from django import forms

from listing.models import (Opportunity, Mandate, Geography, Sector, ValuationFundTicket, Yield, InvestmentOffered,
                            Class, SeriesStage, Category, Country, SubSector, CompanyPurchaseMinMax, InvestorSpecial,
                            FundSize)

from accounts.models import User


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
        fields = ('category', 'investment_sought', 'fund_description', 'fund_size', 'size_ticket_total',
                  'percentage_company_min',
                  'percentage_company_max', 'geography', 'country', 'sector', 'sub_sector', 'yield_select',
                  'growth_expectation_year1',
                  'growth_expectation_year2', 'growth_expectation_year3', 'class_select', 'series_stage',
                  'investor_required', 'fund_size_select')


class OpportunitySearchForm(forms.ModelForm):
    """ Form for search """

    size_ticket_total = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple, queryset=ValuationFundTicket.objects.all(),
            required=False, label='Desired ticket size ($USm)')
    sector = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple, queryset=Sector.objects.all(), required=False, label='Sectors sought')
    yield_select = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple, queryset=Yield.objects.all(), required=False,
            label='Minimum required yield (dividend, interest rate, cap rate)')
    investment_offered = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple, queryset=InvestmentOffered.objects.all(), required=False,
            label='Type of investment sought')
    series_stage = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple, queryset=SeriesStage.objects.all(), required=False,
            label='Series/Stage of investment sought')
    class_select = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple, queryset=Class.objects.all(), required=False,
            label='Asset Class sought')

    class Meta:
        model = Opportunity
        fields = ('size_ticket_total', 'sector', 'class_select', 'yield_select',
                  'series_stage', 'investment_offered')


class MandateChangeListForm(forms.ModelForm):
    # here we only need to define the field we want to be editable
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False)
    investment_sought = forms.ModelMultipleChoiceField(queryset=InvestmentOffered.objects.all(), required=False)
    fund_description = forms.CharField(max_length=500, required=False)
    fund_size = forms.ModelMultipleChoiceField(queryset=ValuationFundTicket.objects.all(), required=False)
    size_ticket_total = forms.ModelMultipleChoiceField(queryset=ValuationFundTicket.objects.all(), required=False)
    percentage_company_min = forms.ModelChoiceField(queryset=CompanyPurchaseMinMax.objects.all(), required=False)
    percentage_company_max = forms.ModelChoiceField(queryset=CompanyPurchaseMinMax.objects.all(), required=False)
    country = forms.ModelMultipleChoiceField(queryset=Country.objects.all(), required=False)
    sub_sector = forms.ModelMultipleChoiceField(queryset=SubSector.objects.all(), required=False)
    yield_select = forms.ModelMultipleChoiceField(queryset=Yield.objects.all(), required=False)
    growth_expectation_year1 = forms.DecimalField(max_digits=15, decimal_places=2, required=False)
    growth_expectation_year2 = forms.DecimalField(max_digits=15, decimal_places=2, required=False)
    growth_expectation_year3 = forms.DecimalField(max_digits=15, decimal_places=2, required=False)
    class_select = forms.ModelMultipleChoiceField(queryset=Class.objects.all(), required=False)
    series_stage = forms.ModelMultipleChoiceField(queryset=SeriesStage.objects.all(), required=False)
    investor_required = forms.ModelChoiceField(queryset=InvestorSpecial.objects.all(), required=False)
    fund_size_select = forms.ModelChoiceField(queryset=FundSize.objects.all(), required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    title = forms.CharField()
    email = forms.EmailField()
    location = forms.CharField()
    user_country = forms.ModelChoiceField(queryset=Country.objects.all())
    fund = forms.CharField()
    mobile = forms.IntegerField()
    land_line = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        if instance:
            initial = kwargs.get('initial', {})
            initial['first_name'] = instance.user.first_name
            initial['last_name'] = instance.user.last_name
            initial['title'] = instance.user.title
            initial['email'] = instance.user.email
            initial['location'] = instance.user.location
            initial['user_country'] = instance.user.country
            initial['fund'] = instance.user.fund
            initial['mobile'] = instance.user.mobile
            initial['land_line'] = instance.user.land_line
            kwargs['initial'] = initial
        super(MandateChangeListForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        # use whatever parsing you like here
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        title = self.cleaned_data['title']
        email = self.cleaned_data['email']
        location = self.cleaned_data['location']
        user_country = self.cleaned_data['user_country']
        fund = self.cleaned_data['fund']
        mobile = self.cleaned_data['mobile']
        land_line = self.cleaned_data['land_line']
        instance = self.instance
        parent_obj = instance.user
        if parent_obj:
            parent_obj.first_name = first_name
            parent_obj.last_name = last_name
            parent_obj.title = title
            parent_obj.email = email
            parent_obj.location = location
            parent_obj.country = user_country
            parent_obj.fund = fund
            parent_obj.mobile = mobile
            parent_obj.land_line = land_line
            # print(" parent_obj  ----> ",  parent_obj)
            parent_obj.save()
        return super(MandateChangeListForm, self).save(*args, **kwargs)
