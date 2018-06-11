from django.db.models import Q
from .models import ValuationFundTicket, Sector, Class, Yield, SeriesStage, InvestmentOffered


def build_lookup_query(field):

    """ Method to build lookup query for Matching Algorithm """

    match_fields = {}
    model = None

    if field == 'size_ticket_total':
        model = ValuationFundTicket
        match_fields = {
            "0-20m": "0-20m, 20-50m",
            "20-50m": "0-20m, 20-50m, 50-100m",
            "50-100m": "20-50m, 50-100m, 100-500m",
            "100-500m": "50-100m, 100-500m, 500-2,000m",
            "500-2,000m": "500-2,000m, 100-500m"
        }

    if field == 'sector':

        model = Sector
        match_fields = {}

    if field == 'class_select':

        model = Class
        match_fields = {
            "Debt": "Debt, Mezz, Equity, Private Equity, Listed Equity, Real Estate",
            "Equity": "Equity, Private Equity, Listed Equity",
            "Private Equity": "Private Equity, Listed Equity, Equity",
            "Listed Equity": "Listed Equity, Equity, Private Equity, Real Estate",
            "Mezz": "Mezz, Debt",
            "Real Estate": "Real Estate, Private Equity, Listed Equity"
        }

    if field == 'yield_select':

        model = Yield
        match_fields = {
            "1-4": "1-4, 4-8",
            "4-8": "1-4, 4-8, 8+",
            "8+": "4-8, 8+",
        }

    if field == 'series_stage':

        model = SeriesStage
        match_fields = {
            "A": "A, B",
            "B": "A, B, C",
            "C": "B, C, Growth",
            "Growth": "C, Growth, Pre-IPO",
            "Pre-IPO": "Growth, Pre-IPO, Feasibility Funding",
            "Feasibility Funding": "Pre-IPO, Feasibility Funding, Construction",
            "Construction": "Feasibility Funding, Construction"
        }

    if field == 'investment_offered':

        model = InvestmentOffered
        match_fields = {
            "Private": "Private, Listed, Direct, Co-Invest",
            "Listed": "Listed, Private, Direct, Co-Invest",
            "Fund": "Fund",
            "Direct": "Direct, Private, Listed, Co-Invest",
            "Co-Invest": "Co-Invest, Private, Listed, Direct, Co-Invest"
        }

    q = Q()
    for field, value in match_fields.items():
        look_up_fields = value.split(",")
        for lookup_field in look_up_fields:
            look_up_obj = model.objects.get(label=lookup_field.strip()).id
            q |= Q(class_select=look_up_obj)
    # match_query = Opportunity.objects.filter(q)
    # return match_query
    return q
