import operator
from functools import reduce

from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.views.generic import DetailView
from django.http import JsonResponse


from listing.forms import OpportunityForm, MandateForm
from listing.models import Mandate, Opportunity, Country, SubSector


class DashboardHome(View):
    """Home dashboard"""
    def get(self, request):

        result = Opportunity.objects.all().order_by('-pk')[:3]
        return render(request, 'dashboard.html', {'result': result})


def save_re(data, instance):
    """ To save High Level Financial's"""

    labels = ["Revenue", "Costs", "EBITDA", "CAPEX", "Net_Profit"]
    years = ["2015A", "2016A", "2017A", "2018E", "2019E"]
    json_data = {}
    for label in labels:
        for yr in years:
            field = "{}_{}".format(label, yr)
            value = data.get(field)
            if field and value:
                json_data[field] = value
    if json_data:
        instance.revenue_json_data = json_data
        instance.save()


class OpportunityUploadView(View):
    """ Listing view """

    def get(self, request):

        return render(request, 'upload.html', {'form': OpportunityForm(), 'opportunity': True})

    def post(self, request):

        form = OpportunityForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            save_re(request.POST, obj)
            return redirect('opportunity-detail-view', obj.id)
        return render(request, 'upload.html', {'form': form, 'opportunity': True})


class MandateUploadView(View):
    """ Mandate upload view"""

    def get(self, request):

        return render(request, 'upload.html', {'form': MandateForm()})

    def post(self, request):

        form = MandateForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('mandate-detail-view', obj.id)
        return render(request, 'upload.html', {'form': form})


class SearchView(View):
    """ Search page view """

    def get(self, request):
        return render(request, 'search_page.html', {'form': OpportunityForm})

    def post(self, request):
        search_result = None
        search_key = request.POST.get('search_key', '')
        search_params = OpportunityForm(request.POST)
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
            search_result = Opportunity.objects.filter(reduce(operator.and_, param_lis))
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


class OpportunityDetailView(DetailView):
    """ Detail view for Opportunity widgets """

    model = Opportunity
    template_name = 'widget_detail.html'
    context_object_name = 'result'


class MandateDetailView(DetailView):
    """ Detail view for Mandate widgets """

    model = Mandate
    template_name = 'widget_detail.html'
    context_object_name = 'result'


def load_cities(request):
    """ Api to load cities wrt Geography """

    geography_id = request.GET.get('geography')
    cities = Country.objects.filter(continent_id=geography_id).values('id', 'country').order_by('country')
    return JsonResponse({'data': list(cities)})


def load_sectors(request):
    """ Api to load sub sectors wrt Sector """

    sector_id = request.GET.get('sector')
    sub_sectors = SubSector.objects.filter(sector_id=sector_id).values('id', 'sub_sector').order_by('sub_sector')
    return JsonResponse({'data': list(sub_sectors)})

