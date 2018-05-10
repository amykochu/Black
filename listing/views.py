from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from listing.forms import ListingForm


class DashboardHome(View):
    """Home dashboard"""
    def get(self, request):
        return render(request, 'dashboard.html', {})


class ListingView(View):
    """ Listing view """

    def get(self, request):

        return render(request, 'listing_view.html', {'form': ListingForm()})

    def post(self, request):

        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'listing_view.html', {'form': form})
