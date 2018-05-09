from django import forms

from listing.models import Listing


class ListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = '__all__'
