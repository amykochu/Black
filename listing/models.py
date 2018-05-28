from django.db import models


class InvestmentOffered(models.Model):

    label = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label


class ValuationFundTicket(models.Model):

    label = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label


class Yield(models.Model):

    label = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label


class Class(models.Model):

    label = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label


class SeriesStage(models.Model):

    label = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label


class InvestorSpecial(models.Model):

    label = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label


class EstPayback(models.Model):

    label = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label


class Offer(models.Model):

    label = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label


class Financial(models.Model):

    label = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label


# class Year(models.Model):
#
#     year1 = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Year 1', blank=True, null=True)
#     year2 = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Year 2', blank=True, null=True)
#     year3 = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Year 3', blank=True, null=True)
#
#     def __str__(self):
#         return str(self.pk)


class Opportunity(models.Model):
    """ Model for opportunity upload """

    company_description = models.CharField(max_length=500, verbose_name='Company / Fund description', blank=True, null=True)
    opportunity_created = models.CharField(max_length=500, verbose_name='What makes this opportunity unique? '
                                                                        'How will value be created/unlocked?', blank=True, null=True)
    selling_by = models.CharField(max_length=500, verbose_name='Who is selling? Why?', blank=True, null=True)
    competitors = models.CharField(max_length=500, verbose_name='Major competitors', blank=True, null=True)
    valuation = models.ManyToManyField(ValuationFundTicket, verbose_name='Valuation - metrics and rationale')
    amount_invested = models.DecimalField(max_digits=5, decimal_places=2,
                                          verbose_name='Amount invested to date ($USm)', blank=True, null=True)
    ownership_structure = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Ownership structure (%)', blank=True, null=True)
    ebitda = models.FloatField(verbose_name='Company EBITDA ($USm)', blank=True, null=True)
    break_even_year = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Break-even year', blank=True, null=True)
    est_payback = models.ManyToManyField(EstPayback, verbose_name='Est. payback on raise')
    size_ticket_total = models.ManyToManyField(ValuationFundTicket, verbose_name='Size ticket total available',
                                               related_name='opportunity_size_ticket')
    #
    geography = models.CharField(max_length=500, verbose_name='Geography', blank=True, null=True)
    #
    sector = models.CharField(max_length=500, verbose_name='Sector', blank=True, null=True)
    yield_select = models.ManyToManyField(Yield, verbose_name='Yield')
    return_estimate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Return estimate (3-yr) (%)', blank=True, null=True)
    #
    growth_expectation = models.CharField(max_length=500, verbose_name='Earnings growth expectation (%)', blank=True, null=True)
    class_select = models.ManyToManyField(Class, verbose_name='Class')
    series_stage = models.ManyToManyField(SeriesStage, verbose_name='Series/stage')
    investor_required = models.ManyToManyField(InvestorSpecial, verbose_name='Lead Investor required in place')
    amount_lead_partner = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Amount injected by Lead Partner', blank=True, null=True)
    amount_other_partner = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Amount injected by Other Partners', blank=True, null=True)
    amount_weraise = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Amount available for WeRaise', blank=True, null=True)
    investment_offered = models.ManyToManyField(InvestmentOffered, verbose_name='Type of investment offered')
    offer = models.ManyToManyField(Offer, verbose_name='Offer')
    special_situation = models.ManyToManyField(InvestorSpecial, verbose_name='Special situation',
                                               related_name='special_situation')
    financials = models.ManyToManyField(Financial, verbose_name='Financials')
    #
    Revenue = models.CharField(max_length=500, verbose_name='Revenue', blank=True, null=True)
    estimated_irr = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Estimated IRR', blank=True, null=True)
    exit_timing = models.CharField(max_length=500, verbose_name='Expected exit timing', blank=True, null=True)
    use_of_funds = models.CharField(max_length=500, verbose_name='Use of funds', blank=True, null=True)
    deadline_commitment = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Deadline for formal commitment', blank=True, null=True)
    deadline_legal = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Deadline for execution of legal docs', blank=True, null=True)
    proposed_process = models.CharField(max_length=500, verbose_name='Proposed process', blank=True, null=True)
    proposed_exit = models.CharField(max_length=500, verbose_name='Proposed exit options', blank=True, null=True)
    financial_statements = models.FileField(upload_to='listing/documents/',
                                            verbose_name='Do you have 3 years audited financial statements available?', blank=True, null=True)
    financial_model = models.FileField(upload_to='listing/documents/', verbose_name='Do you have a financial model?', blank=True, null=True)
    investor_deck = models.FileField(upload_to='listing/documents/', verbose_name='Do you have an investor deck?', blank=True, null=True)
    company_bio = models.TextField(max_length=500, verbose_name='Company Bio', blank=True, null=True)
    ceo_bio = models.TextField(max_length=500, verbose_name='CEO Bio', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)


class Mandate(models.Model):
    """ Model to upload Mandate """

    investment_sought = models.ManyToManyField(InvestmentOffered, verbose_name='Type of investment sought')
    fund_size = models.ManyToManyField(ValuationFundTicket, verbose_name='Required company or fund size')
    size_ticket_total = models.ManyToManyField(ValuationFundTicket, verbose_name='Desired ticket size',
                                               related_name='mandate_size_ticket')
    percentage_company = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='% of company (min - max)')
    #
    geography = models.CharField(max_length=500, verbose_name='Geography')
    #
    sector = models.CharField(max_length=500, verbose_name='Sector')
    yield_select = models.ManyToManyField(Yield, verbose_name='Yield')
    #
    growth_required = models.CharField(max_length=500, verbose_name='Earnings growth required (%)')
    class_select = models.ManyToManyField(Class, verbose_name='Class')
    series_stage = models.ManyToManyField(SeriesStage, verbose_name='Series/stage')
    investor_required = models.ManyToManyField(InvestorSpecial, verbose_name='Lead Investor required in place')
