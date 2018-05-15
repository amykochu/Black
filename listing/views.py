import operator
from functools import reduce

from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.views.generic import DetailView

from listing.forms import ListingForm, SearchForm
from listing.models import Listing


class DashboardHome(View):
    """Home dashboard"""
    def get(self, request):

        result = Listing.objects.all().order_by('-pk')[:3]
        return render(request, 'dashboard.html', {'result': result})


class UploadView(View):
    """ Listing view """

    def get(self, request):

        return render(request, 'upload.html', {'form': ListingForm()})

    def post(self, request):

        form = ListingForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('detail-view', obj.id)
        return render(request, 'upload.html', {'form': form})


class SearchView(View):
    """ Search page view """

    def get(self, request):
        return render(request, 'search_page.html', {'form': SearchForm})

    def post(self, request):
        search_result = None
        search_key = request.POST.get('search_key', '')
        search_params = SearchForm(request.POST)
        if search_params.is_valid():
            widget7 = search_params.cleaned_data['widget7']
            # widget8 = search_params.cleaned_data['widget8']
            # widget9 = search_params.cleaned_data['widget9']
            widget10 = search_params.cleaned_data['widget10']
            widget11 = search_params.cleaned_data['widget11']
            widget12 = search_params.cleaned_data['widget12']
            # widget13 = search_params.cleaned_data['widget13']
            widget15 = search_params.cleaned_data['widget15']
            param_lis = [Q(widget7__icontains=widget7),
                         Q(widget10__icontains=widget10),
                         Q(widget11__icontains=widget11),
                         Q(widget12__icontains=widget12),
                         Q(widget15__icontains=widget15)]
            search_result = Listing.objects.filter(reduce(operator.and_, param_lis))
        if search_key:
            search_result = search_result.filter(Q(widget1__icontains=search_key) |
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
                                                   Q(widget19__icontains=search_key)).distinct()

        return render(request, 'search_page.html', {'result': search_result, 'form': search_params})


class WidgetDetailView(DetailView):
    """ Detail view for Widgets """

    model = Listing
    template_name = 'widget_detail.html'
    context_object_name = 'result'

