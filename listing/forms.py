from django import forms

from listing.models import Opportunity, Mandate, Country, Geography, SubSector


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

    class Meta:
        model = Opportunity
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country'].queryset = Country.objects.none()
        self.fields['sub_sector'].queryset = SubSector.objects.none()


class MandateForm(forms.ModelForm):
    """ Form for Investor Mandate upload """

    class Meta:
        model = Mandate
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country'].queryset = Country.objects.none()
        self.fields['sub_sector'].queryset = SubSector.objects.none()
