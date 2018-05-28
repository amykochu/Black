from django import forms

from listing.models import Opportunity, Mandate, VALUATION_FUND_TICKET_CHOICES


# class ListingForm(forms.ModelForm):
#     """ Form to upload data """
#
#     widget6 = forms.MultipleChoiceField(choices=Listing.WIDGET_6_CHOICES)
#
#     class Meta:
#         model = Listing
#         fields = '__all__'


# class SearchForm(forms.ModelForm):
#     """ Form for search """
#
#     class Meta:
#         model = Listing
#         fields = {'widget7', 'widget10', 'widget11', 'widget12', 'widget15'}
#
#     def __init__(self, *args, **kwargs):
#         super(SearchForm, self).__init__(*args, **kwargs)
#         self.fields['widget7'].required = False
#         # self.fields['widget8'].required = False
#         # self.fields['widget9'].required = False
#         self.fields['widget10'].required = False
#         self.fields['widget11'].required = False
#         self.fields['widget12'].required = False
#         # self.fields['widget13'].required = False
#         self.fields['widget15'].required = False


class OpportunityForm(forms.ModelForm):
    """ Form to upload Opportunity data """

    est_payback = forms.MultipleChoiceField(choices=Opportunity.EST_PAYBACK_CHOICES)
    size_ticket_total = forms.MultipleChoiceField(choices=VALUATION_FUND_TICKET_CHOICES)

    class Meta:
        model = Opportunity
        fields = '__all__'


class MandateForm(forms.ModelForm):
    """ Form for Investor Mandate upload """

    class Meta:
        model = Mandate
        fields = '__all__'
