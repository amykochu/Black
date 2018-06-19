import xlrd
import mmap

from listing.models import (Opportunity, Mandate, InvestmentOffered, ValuationFundTicket, Yield, Class,
                            SeriesStage, InvestorSpecial, EstPayback, Offer, Financial, Country, Geography,
                            SubSector, Sector, CompanyPurchaseMinMax)


def xls_dict_reader(f, sheet_index=0):
    book = xlrd.open_workbook(file_contents=mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ))
    sheet = book.sheet_by_index(sheet_index)
    headers = dict((i, sheet.cell_value(0, i)) for i in range(sheet.ncols))
    data_dict = (dict((headers[j], sheet.cell_value(i, j)) for j in headers) for i in range(1, sheet.nrows))

    for data in data_dict:
        print(data.keys())
