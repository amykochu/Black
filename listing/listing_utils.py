import xlrd
import mmap

from django.contrib.auth.models import User

from listing.models import (Mandate, InvestmentOffered, ValuationFundTicket, Yield, Class,
                            SeriesStage, InvestorSpecial, Country, Geography,
                            SubSector, Sector, CompanyPurchaseMinMax)


def xls_dict_reader(f, sheet_index=0):
    book = xlrd.open_workbook(file_contents=mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ))
    sheet = book.sheet_by_index(sheet_index)
    headers = dict((i, sheet.cell_value(0, i)) for i in range(sheet.ncols))
    data_dict = (dict((headers[j], sheet.cell_value(i, j)) for j in headers) for i in range(1, sheet.nrows))

    for data in data_dict:
        investment_obj = fund_size_obj = ticket_size_obj = percentage_company_max = percentage_company_min = \
            country_obj = sub_sector_obj = required_yield_obj = earnings_growth_1 = earnings_growth_2 = \
            earnings_growth_3 = asset_class_obj = series_stage_obj = lead_investor_obj = None

        if data['Geography sought']:
            geography_list = data['Geography sought'].split(", ")
            if 'ALL' in geography_list:
                geography_obj = Geography.objects.all()
                country_obj = Country.objects.filter(continent__in=geography_obj)
            else:
                geography_obj = Geography.objects.filter(continent__in=geography_list)
                country_obj = Country.objects.filter(continent__in=geography_obj)

        if data['Country']:
            country_list = data['Country'].split(", ")
            country_obj = Country.objects.filter(country__in=country_list)

        if data['Type of Investment sought']:
            investment = data['Type of Investment sought'].split(", ")
            if 'ALL' in investment:
                investment_obj = InvestmentOffered.objects.all()
            else:
                investment_obj = InvestmentOffered.objects.filter(label__in=investment)

        if data['Required minimum company or fund size ($USm)']:
            fund_size = data['Required minimum company or fund size ($USm)'].split(", ")
            if 'ALL' in fund_size:
                fund_size_obj = ValuationFundTicket.objects.all()
            else:
                fund_size_obj = ValuationFundTicket.objects.filter(label__in=fund_size)

        if data['Desired ticket size ($USm)']:
            ticket_size = data['Desired ticket size ($USm)'].split(", ")
            if 'ALL' in ticket_size:
                ticket_size_obj = ValuationFundTicket.objects.all()
            else:
                ticket_size_obj = ValuationFundTicket.objects.filter(label__in=ticket_size)

        if data['Sectors sought']:
            sector = data['Sectors sought'].split(", ")
            if 'ALL' in sector:
                sector_obj = Sector.objects.all()
            else:
                sector_obj = Sector.objects.filter(sector__in=sector)
            sub_sector_obj = SubSector.objects.filter(sector__in=sector_obj)

        if data['Series/stage of investment sought']:
            series_stage = data['Series/stage of investment sought'].split(", ")
            if 'ALL' in series_stage:
                series_stage_obj = SeriesStage.objects.all()
            else:
                series_stage_obj = SeriesStage.objects.filter(label__in=series_stage)

        if data['Asset class sought']:
            asset_class = data['Asset class sought'].split(", ")
            if 'ALL' in asset_class:
                asset_class_obj = Class.objects.all()
            else:
                asset_class_obj = Class.objects.filter(label__in=asset_class)

        if data['Minimum required yield (dividend, interest rate, cap rate)']:
            required_yield = data['Minimum required yield (dividend, interest rate, cap rate)']
            try:
                required_yield_obj = Yield.objects.get(label=required_yield)
            except:
                pass

        if data['Minimum earnings growth required (%, FY1, FY2, FY3)']:
            earnings_growth = data['Minimum earnings growth required (%, FY1, FY2, FY3)'].replace('%', '').split(", ")
            earnings_growth_1 = earnings_growth[0]
            earnings_growth_2 = earnings_growth[1]
            earnings_growth_3 = earnings_growth[2]

        if data['% of company/fund can purchase/hold (min-max)']:
            percentage_company = data['% of company/fund can purchase/hold (min-max)'].replace('%', '').split('-')
            try:
                percentage_company_max = CompanyPurchaseMinMax.objects.get(label=percentage_company[1]+'%')
                percentage_company_min = CompanyPurchaseMinMax.objects.get(label=percentage_company[0]+'%')
            except:
                pass

        if data['Lead Investor required in place']:
            lead_investor = data['Lead Investor required in place'].upper()
            try:
                lead_investor_obj = InvestorSpecial.objects.get(label=lead_investor)
            except:
                pass
        user = User.objects.get(id=1)
        # Creating mandate object
        mandate, create = Mandate.objects.get_or_create(user=user,
                               percentage_company_min=percentage_company_min,
                               percentage_company_max=percentage_company_max,
                               yield_select=required_yield_obj,
                               growth_expectation_year1=earnings_growth_1, growth_expectation_year2=earnings_growth_2,
                               growth_expectation_year3=earnings_growth_3, investor_required=lead_investor_obj)
        mandate.investment_sought_set = investment_obj
        mandate.fund_size_set = fund_size_obj
        mandate.size_ticket_total_set = ticket_size_obj
        mandate.country_set = country_obj
        mandate.sub_sector_set = sub_sector_obj
        mandate.class_select_set = asset_class_obj
        mandate.series_stage_set = series_stage_obj
        mandate.save()
