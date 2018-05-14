from django import forms

from listing.models import Listing


class ListingForm(forms.ModelForm):
    """ Form to upload data """

    class Meta:
        model = Listing
        fields = '__all__'


class SearchForm(forms.ModelForm):
    """ Form for search """

    class Meta:
        model = Listing
        fields = {'widget7', 'widget8', 'widget9', 'widget10', 'widget11', 'widget12', 'widget13', 'widget15'}

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['widget7'].required = False
        self.fields['widget8'].required = False
        self.fields['widget9'].required = False
        self.fields['widget10'].required = False
        self.fields['widget11'].required = False
        self.fields['widget12'].required = False
        self.fields['widget13'].required = False
        self.fields['widget15'].required = False
