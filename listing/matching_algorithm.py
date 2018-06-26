from django.db.models import Q
from .models import ValuationFundTicket, Sector, Class, Yield, SeriesStage, InvestmentOffered, Mandate, Opportunity


def match(mandate_obj):
    """ Method for matching profiles wrt to mandate object """

    if isinstance(mandate_obj, Mandate):
        match_data = Opportunity.objects.all()

        get_class_q = build_lookup_query('class_select', mandate_obj.class_select.all().values_list('label', flat=True))
        get_size_ticket_total_q = build_lookup_query('size_ticket_total', mandate_obj.size_ticket_total.all().
                                                     values_list('label', flat=True))
        # get_yield_select_q = build_lookup_query('yield_select', [mandate_obj.yield_select.label])
        get_yield_select_q = build_lookup_query('yield_select',
                                                mandate_obj.yield_select.all().values_list('label', flat=True))
        get_series_stage_q = build_lookup_query('series_stage', mandate_obj.series_stage.all().
                                                values_list('label', flat=True))
        get_investment_offered_q = build_lookup_query('investment_offered', mandate_obj.investment_sought.all().
                                                      values_list('label', flat=True))
        d = set()
        d.update(mandate_obj.sub_sector.all().values_list("sector__sector", flat=True))
        get_sector_q = build_lookup_query('sector', list(d))
        match_data = match_data.filter(get_class_q & get_size_ticket_total_q & get_series_stage_q &
                                       get_investment_offered_q & get_yield_select_q & get_sector_q).distinct()
        return match_data


def build_lookup_query(field, field_values):
    """ Method to build lookup query for Matching Algorithm """
    match_fields = {}
    model = None

    if field == 'size_ticket_total':
        model = ValuationFundTicket
        match_fields = {
            "0-20m": "0-20m,20-50m",
            "20-50m": "0-20m,20-50m,50-100m",
            "50-100m": "20-50m,50-100m,100-500m",
            "100-500m": "50-100m,100-500m,500-2,000m",
            "500-2,000m": "500-2,000m,100-500m"
        }

    if field == 'sector':
        model = Sector
        match_fields = {
            "Energy": "Energy,Materials",
            "Materials": "Materials,Energy",
            "Industrials": "Industrials",
            "Consumer Discretionary": "Consumer Discretionary,Consumer Staples",
            "Consumer Staples": "Consumer Staples,Consumer Discretionary",
            "Health Care": "Health Care",
            "Financials": "Financials",
            "Information Technology": "Information Technology",
            "Telecommunication Services": "Telecommunication Services",
            "Utilities": "Utilities",
            "Real Estate": "Real Estate"
        }

    if field == 'class_select':
        model = Class
        match_fields = {
            "Debt": "Debt,Mezz,Private Equity",
            "Equity": "Equity,Private Equity,Listed Equity",
            "Private Equity": "Private Equity,Listed Equity,Equity",
            "Listed Equity": "Listed Equity,Equity,Private Equity,Real Estate",
            "Mezz": "Mezz,Debt",
            "Real Estate": "Real Estate,Private Equity,Listed Equity"
        }

    if field == 'yield_select':

        model = Yield
        match_fields = {
            "1-4": "1-4,4-8",
            "4-8": "1-4,4-8,8+",
            "8+": "4-8,8+",
        }

    if field == 'series_stage':

        model = SeriesStage
        match_fields = {
            "A": "A,B",
            "B": "A,B,C",
            "C": "B,C,Growth",
            "Growth": "C,Growth,Pre-IPO",
            "Pre-IPO": "Growth,Pre-IPO,Feasibility Funding",
            "Feasibility Funding": "Pre-IPO,Feasibility Funding,Construction",
            "Construction": "Feasibility Funding,Construction"
        }

    if field == 'investment_offered':

        model = InvestmentOffered
        match_fields = {
            "Private": "Private,Listed,Direct,Co-Invest",
            "Listed": "Listed,Private,Direct,Co-Invest",
            "Fund": "Fund,Co-Invest",
            "Direct": "Direct,Private,Listed,Co-Invest",
            "Co-Invest": "Co-Invest,Private,Listed,Direct,Co-Invest"
        }

    label_set = set()
    for k in field_values:
        for i, j in match_fields.items():
            if k == i:
                label_set.update(j.split(','))
    label_list = list(label_set)

    q = Q()
    for label_field in label_list:
        try:
            if field == 'sector':
                look_up_obj = model.objects.get(sector=label_field.strip())
                field_dict = {'sub_sector__sector__sector': look_up_obj}
            else:
                look_up_obj = model.objects.get(label=label_field.strip())
                field_dict = {field: look_up_obj}
            q |= Q(**field_dict)
        except:
            continue
    return q
