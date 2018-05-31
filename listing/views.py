import operator
from functools import reduce

from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.views.generic import DetailView
from django.http import JsonResponse


from listing.forms import OpportunityForm, MandateForm, OpportunitySearchForm
from listing.models import Mandate, Opportunity, Country, SubSector


class DashboardHome(View):
    """Home dashboard"""
    def get(self, request):

        result = Opportunity.objects.all().order_by('-pk')[:12]
        return render(request, 'dashboard.html', {'result': result})


def save_re(data):
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
    return json_data


class OpportunityUploadView(View):
    """ Listing view """

    def get(self, request):

        return render(request, 'upload.html', {'form': OpportunityForm(), 'opportunity': True})

    def post(self, request):

        json_data = save_re(request.POST)
        form = OpportunityForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            if json_data:
                obj.revenue_json_data = json_data
                obj.save()
            FindMatch(obj)
            # return redirect('opportunity-detail-view', obj.id)
        return render(request, 'upload.html', {'form': form, 'opportunity': True, 'json_data': json_data})


class MandateUploadView(View):
    """ Mandate upload view"""

    def get(self, request):

        return render(request, 'upload.html', {'form': MandateForm()})

    def post(self, request):

        form = MandateForm(request.POST)
        if form.is_valid():
            obj = form.save()
            # FindMatch(obj)
            return redirect('mandate-detail-view', obj.id)
        return render(request, 'upload.html', {'form': form})


class SearchView(View):
    """ Search page view """

    def get(self, request):

        search_result = None
        search_key = request.GET.get('search_key', '')
        search_params = OpportunitySearchForm(request.GET)
        if search_params.is_valid():
            geography = search_params.cleaned_data['geography']
            country = search_params.cleaned_data['country']
            sector = search_params.cleaned_data['sector']
            sub_sector = search_params.cleaned_data['sub_sector']
            yield_select = search_params.cleaned_data['yield_select']
            size_ticket_total = search_params.cleaned_data['size_ticket_total']
            return_estimate = search_params.cleaned_data['return_estimate']
            class_select = search_params.cleaned_data['class_select']

            # print("geography  === ", geography)
            # param_lis = [Q(widget7__icontains=widget7),
            #              Q(widget10__icontains=widget10),
            #              Q(widget11__icontains=widget11),
            #              Q(widget12__icontains=widget12),
            #              Q(widget15__icontains=widget15)]
            # search_result = Opportunity.objects.filter(reduce(operator.and_, param_lis))
        if search_key:
            print("SE KEY", search_key)
            search_result = Opportunity.objects.filter(Q(company_description__icontains=search_key) |
                                                       Q()).distinct()
        return render(request, 'search_page.html', {'result': search_result, 'form': OpportunitySearchForm})


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


def FindMatch(profile):
    """ Matching Algorithm """
    print("INSIDE MATCH   ============= ")
    match_data = None
    is_opportunity = isinstance(profile, Opportunity)
    is_mandate = isinstance(profile, Mandate)

    if is_opportunity:
        # sector and yield
        match_params = [Q(investment_sought__icontains=profile.investment_offered),
                         Q(size_ticket_total__icontains=profile.size_ticket_total),
                         Q(sector__sector__icontains=profile.sector.sector),
                         Q(sub_sector__icontains=profile.sub_sector),
                         Q(class_select__icontains=profile.class_select),
                         Q(series_stage__icontains=profile.series_stage),
                         Q(yield_select__label__icontains=profile.yield_select.label)
                        ]
        match_data = Mandate.objects.filter(reduce(operator.or_, match_params)).distinct()
    if is_mandate:
        match_params = [Q(investment_offered__=profile.investment_sought),
                         Q(size_ticket_total__icontains=profile.size_ticket_total),
                         Q(sector__sector__icontains=profile.sector.sector),
                         Q(sub_sector__icontains=profile.sub_sector),
                         Q(class_select__icontains=profile.class_select),
                         Q(series_stage__icontains=profile.series_stage),
                         Q(yield_select__label__icontains=profile.yield_select.label)
                        ]
        match_data = Opportunity.objects.filter(reduce(operator.and_, match_params)).distinct()
    return render('results.html', {'match_results': match_data})
