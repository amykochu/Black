from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from listing.forms import ListingForm
from listing.models import Listing
from django.db.models import Q

from django.views.generic import TemplateView, DetailView, ListView


class DashboardHome(View):
    """Home dashboard"""
    def get(self, request):
        return render(request, 'dashboard.html', {})


class UploadView(View):
    """ Listing view """

    def get(self, request):

        return render(request, 'upload.html', {'form': ListingForm()})

    def post(self, request):

        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'upload.html', {'form': form})


class SearchView(View):
    """ Search page view """

    # context_object_name = 'result'
    # template_name = 'search_page.html'

    # def get_queryset(self):
    #     return Listing.objects.all()

    def get(self, request):
        return render(request, 'search_page.html', {})

    def post(self, request):
        search_key = request.POST.get('search_key', '')
        search_result = Listing.objects.filter(Q(widget1__icontains=search_key) |
                                               Q(widget2__icontains=search_key) |
                                               Q(widget3__icontains=search_key) |
                                               Q(widget4__icontains=search_key) |
                                               Q(widget5__icontains=search_key) |
                                               Q(widget6__icontains=search_key) |
                                               Q(widget7__icontains=search_key) |
                                               Q(widget8__widget_choice__icontains=search_key) |
                                               Q(widget9__widget_choice__icontains=search_key) |
                                               Q(widget10__icontains=search_key) |
                                               Q(widget11__icontains=search_key) |
                                               Q(widget12__icontains=search_key) |
                                               Q(widget13__widget_choice__icontains=search_key) |
                                               Q(widget14__widget_choice__icontains=search_key) |
                                               Q(widget15__icontains=search_key) |
                                               Q(widget16__icontains=search_key) |
                                               Q(widget17__widget_choice__icontains=search_key) |
                                               Q(widget18__icontains=search_key) |
                                               Q(widget19__icontains=search_key))
        return render(request, 'search_page.html', {'result': search_result})
