from django import forms

from listing.models import Opportunity, Mandate, Country, Geography, SubSector


class OpportunityForm(forms.ModelForm):
    """ Form to upload Opportunity data """
    class Meta:
        model = Opportunity
        exclude = ('revenue_json_data', )


class MandateForm(forms.ModelForm):
    """ Form for Investor Mandate upload """

    class Meta:
        model = Mandate
        fields = '__all__'


class OpportunitySearchForm(forms.ModelForm):
    """ Form for search """

    class Meta:
        model = Opportunity
        fields = {'geography', 'country', 'sector', 'sub_sector', 'yield_select',
                  'ceo_bio', 'size_ticket_total', 'return_estimate', 'class_select'}

    def __init__(self, *args, **kwargs):
        super(OpportunitySearchForm, self).__init__(*args, **kwargs)
        self.fields['geography'].required = False
        self.fields['country'].required = False
        self.fields['sector'].required = False
        self.fields['sub_sector'].required = False
        self.fields['yield_select'].required = False
        self.fields['size_ticket_total'].required = False
        self.fields['class_select'].required = False

        self.fields['return_estimate'].required = False
        # self.fields['size_ticket_total'].required = False
        # self.fields['size_ticket_total'].required = False
