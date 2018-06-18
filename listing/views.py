import operator
from functools import reduce

from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.views.generic import DetailView
from django.http import JsonResponse

from listing.matching_algorithm import match

from listing.forms import OpportunityForm, MandateForm, OpportunitySearchForm
from listing.models import Mandate, Opportunity, Country, SubSector, Geography, Sector


class DashboardHome(View):
    """Home dashboard"""
    def get(self, request):

        result = set()
        if request.user:

            user = request.user
            mandates = Mandate.objects.filter(user=user)
            for mandate in mandates:
                result.update(match(mandate))

            search_params = request.GET.get('size_ticket_total', '')
            if search_params:
                # result = refine_search(search_params, result)
                pass
        return render(request, 'dashboard.html', {'result': list(result), 'dashboard': True,
                                                  'search_form': OpportunitySearchForm})


def refine_search(search_params, result):

    return ""


def save_re(data):
    """ To save High Level Financial's"""

    labels = ["Revenue", "Costs", "EBITDA", "CAPEX", "Net_Profit"]
    years = ["2015A", "2016A", "2017A", "2018E", "2019E", "2020E"]
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

        post_data = request.POST.copy()
        json_data = save_re(request.POST)
        post_data.setlist('est_payback', remove_zero(post_data, 'est_payback'))
        post_data.setlist('offer', remove_zero(post_data, 'offer'))
        post_data.setlist('investment_sought', remove_zero(post_data, 'investment_sought'))
        post_data.setlist('fund_size', remove_zero(post_data, 'fund_size'))
        post_data.setlist('size_ticket_total', remove_zero(post_data, 'size_ticket_total'))
        post_data.setlist('geography', remove_zero(post_data, 'geography'))
        post_data.setlist('country', remove_zero(post_data, 'country'))
        post_data.setlist('sector', remove_zero(post_data, 'sector'))
        post_data.setlist('sub_sector', remove_zero(post_data, 'sub_sector'))
        post_data.setlist('class_select', remove_zero(post_data, 'class_select'))
        post_data.setlist('series_stage', remove_zero(post_data, 'series_stage'))
        form = OpportunityForm(post_data, request.FILES)
        if form.is_valid():
            obj = form.save()
            if json_data:
                obj.revenue_json_data = json_data
                obj.save()
            # match_data = FindMatch(obj)
            # return render(request, 'results.html', {'match_data': match_data})
            return redirect('/')
        return render(request, 'upload.html', {'form': form, 'opportunity': True, 'json_data': json_data})


class MandateUploadView(View):
    """ Mandate upload view"""

    def get(self, request):

        return render(request, 'upload.html', {'form': MandateForm(), 'mandate': True})

    def post(self, request):

        post_data = request.POST.copy()
        post_data.setlist('investment_sought', remove_zero(post_data, 'investment_sought'))
        post_data.setlist('fund_size', remove_zero(post_data, 'fund_size'))
        post_data.setlist('size_ticket_total', remove_zero(post_data, 'size_ticket_total'))
        post_data.setlist('geography', remove_zero(post_data, 'geography'))
        post_data.setlist('country', remove_zero(post_data, 'country'))
        post_data.setlist('sector', remove_zero(post_data, 'sector'))
        post_data.setlist('sub_sector', remove_zero(post_data, 'sub_sector'))
        post_data.setlist('class_select', remove_zero(post_data, 'class_select'))
        post_data.setlist('series_stage', remove_zero(post_data, 'series_stage'))
        form = MandateForm(post_data)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            form.save_m2m()
            return redirect('/')
            # match_data = match(obj)
            # return render(request, 'dashboard.html', {'result': match_data, 'dashboard': True,
            #                                           'search_form': OpportunitySearchForm})
        return render(request, 'upload.html', {'form': form, 'mandate': True})


def remove_zero(post_data, field):
    """ Method to remove 0 from many2many - select all"""

    field_list = post_data.getlist(field)
    if '0' in field_list:
        field_list.remove('0')
    return field_list


# class SearchView(View):
#     """ Search page view """
#
#     def get(self, request):
#
#         search_result = None
#         search_key = request.GET.get('search_key', '')
#         search_params = OpportunitySearchForm(request.GET)
#         if search_params.is_valid():
#             geography = search_params.cleaned_data['geography']
#             country = search_params.cleaned_data['country']
#             sector = search_params.cleaned_data['sector']
#             sub_sector = search_params.cleaned_data['sub_sector']
#             yield_select = search_params.cleaned_data['yield_select']
#             size_ticket_total = search_params.cleaned_data['size_ticket_total']
#             return_estimate = search_params.cleaned_data['return_estimate']
#             class_select = search_params.cleaned_data['class_select']
#
#             # print("geography  === ", geography)
#             # param_lis = [Q(widget7__icontains=widget7),
#             #              Q(widget10__icontains=widget10),
#             #              Q(widget11__icontains=widget11),
#             #              Q(widget12__icontains=widget12),
#             #              Q(widget15__icontains=widget15)]
#             # search_result = Opportunity.objects.filter(reduce(operator.and_, param_lis))
#         if search_key:
#             print("SE KEY", search_key)
#             search_result = Opportunity.objects.filter(Q(company_description__icontains=search_key) |
#                                                        Q()).distinct()
#         return render(request, 'search_page.html', {'result': search_result, 'form': OpportunitySearchForm})


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

    geo_id = request.GET.get('geography')
    cities = Country.objects.filter(continent_id=geo_id).values('id', 'country').order_by('country')
    continent = Geography.objects.get(pk=geo_id).continent
    return JsonResponse({'data': list(cities), 'continent': continent})


def load_sectors(request):
    """ Api to load sub sectors wrt Sector """
    sector_id = request.GET.get('sector')
    sub_sectors = SubSector.objects.filter(sector_id=sector_id).values('id', 'sub_sector').order_by('sub_sector')
    sector = Sector.objects.get(pk=sector_id).sector
    return JsonResponse({'data': list(sub_sectors), 'sector': sector})


def FindMatch(profile):
    """ Matching Algorithm """
    match_data = None
    is_mandate = isinstance(profile, Mandate)

    if is_mandate:
        match_data = Opportunity.objects.all()
        invest_id_list = list(profile.investment_sought.all().values_list('id', flat=True))
        size_ticket_list = list(profile.size_ticket_total.all().values_list('id', flat=True))
        class_select_list = list(profile.class_select.all().values_list('id', flat=True))
        series_stage_list = list(profile.series_stage.all().values_list('id', flat=True))

        # sector_list = list(profile.sector.all().values_list('id', flat=True))
        yield_select_list = [profile.yield_select_id]
        # sector_list = [profile.sector_id]

        d = {'investment_offered__id': invest_id_list, 'size_ticket_total__id': size_ticket_list,
             'class_select__id': class_select_list, 'series_stage__id': series_stage_list,
             'yield_select__id': yield_select_list, }
        # 'sector__id': sector_list}
        for k, v in d.items():
            for i in v:
                d2 = {k: i}
                match_data = match_data.filter(**d2)
    return match_data
    # return render(request, 'results.html', {'match_data': match_data})
