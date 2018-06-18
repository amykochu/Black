from django.utils import timezone

from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User


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


class Geography(models.Model):
    """ Model to store Geographic region """

    continent = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.continent

    class Meta:
        ordering = ['continent']


class Country(models.Model):
    """ Model to store Country """

    country = models.CharField(max_length=300)
    continent = models.ForeignKey(Geography, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country


class Sector(models.Model):
    """ Model to store Sectors """

    sector = models.CharField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sector

    class Meta:
        ordering = ['sector']


class SubSector(models.Model):
    """ Model to store Sub Sectors """

    sub_sector = models.CharField(max_length=300)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sub_sector


class Opportunity(models.Model):
    """ Model for opportunity upload """

    company_description = models.CharField(max_length=500, verbose_name='Company / Fund description')
    opportunity_created = models.CharField(max_length=500, verbose_name='What makes this opportunity unique? '
                                                                        'How will value be created/unlocked?')
    selling_by = models.CharField(max_length=500, verbose_name='Who is selling? Why?')
    competitors = models.CharField(max_length=500, verbose_name='Major competitors')
    valuation = models.ForeignKey(ValuationFundTicket,  on_delete=models.SET_NULL, null=True, verbose_name='Company valuation - metrics and rationale ($USm)')
    valuation_text = models.CharField(max_length=200, verbose_name='Company valuation - metrics and rationale (Input)')
    amount_invested = models.DecimalField(max_digits=15, decimal_places=2,
                                          verbose_name='Amount invested to date ($USm)')
    ownership_structure = models.CharField(max_length=300, verbose_name='Ownership structure (%), Major shareholders (%)')
    ebitda = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Company EBITDA ($USm)')
    break_even_year = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Break-even year')
    est_payback = models.ManyToManyField(EstPayback, verbose_name='Estimated payback period on raise')
    size_ticket_total = models.ManyToManyField(ValuationFundTicket, verbose_name='Size ticket input',
                                               related_name='opportunity_size_ticket')
    #
    # geography = models.ForeignKey(Geography, on_delete=models.SET_NULL, null=True)
    country = models.ManyToManyField(Country)
    #
    # sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, verbose_name='Sector', blank=True, null=True)
    sub_sector = models.ManyToManyField(SubSector, verbose_name='Sub Sector')
    yield_select = models.ForeignKey(Yield, on_delete=models.SET_NULL, verbose_name='Yield', null=True)
    return_estimate = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Return estimate forecast (3-yr) (%)')
    growth_expectation_year1 = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Earnings expectation forecast ($USm FY1)')
    growth_expectation_year2 = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Earnings expectation forecast ($USm FY2)')
    growth_expectation_year3 = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Earnings expectation forecast ($USm FY3)')
    class_select = models.ManyToManyField(Class, verbose_name='Asset class')
    series_stage = models.ManyToManyField(SeriesStage, verbose_name='Series/stage of investment')
    investor_required = models.ForeignKey(InvestorSpecial, on_delete=models.CASCADE, verbose_name='Is there a lead investor?', null=True)
    amount_lead_partner = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Amount injected by Lead Partner ($USm)')
    amount_other_partner = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Amount injected by Other Partners ($USm)')
    amount_weraise = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Amount available for WeRaise ($USm)')
    investment_offered = models.ManyToManyField(InvestmentOffered, verbose_name='Type of investment offered')
    offer = models.ManyToManyField(Offer, verbose_name='Offer')
    special_situation = models.ForeignKey(InvestorSpecial, on_delete=models.CASCADE, verbose_name='Special situation',
                                               related_name='special_situation', null=True)
    financials = models.ForeignKey(Financial, on_delete=models.SET_NULL, verbose_name='Financials (currency)', null=True)
    #
    revenue_json_data = JSONField(blank=True, null=True)
    estimated_irr = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Estimated IRR')
    exit_timing = models.CharField(max_length=500, verbose_name='Expected exit timing')
    use_of_funds = models.CharField(max_length=500, verbose_name='Use of funds')
    deadline_commitment = models.DateTimeField(default=timezone.now, verbose_name='Deadline for formal commitment')
    deadline_legal = models.DateTimeField(default=timezone.now, verbose_name='Deadline for execution of legal docs')
    proposed_process = models.CharField(max_length=500, verbose_name='Proposed capital raise process')
    proposed_exit = models.CharField(max_length=500, verbose_name='Proposed exit options')
    financial_statements = models.FileField(upload_to='listing/documents/',
                                            verbose_name='Do you have 3 years audited financial statements available?',
                                            validators=[FileExtensionValidator(allowed_extensions=['xls', 'xlsx', 'pdf'])],
                                            blank=True, null=True)
    financial_model = models.FileField(upload_to='listing/documents/', verbose_name='Do you have a financial model?',
                                       validators=[FileExtensionValidator(allowed_extensions=['xls', 'xlsx', 'pdf'])],
                                       blank=True, null=True)
    investor_deck = models.FileField(upload_to='listing/documents/', verbose_name='Do you have an investor deck?',
                                     validators=[FileExtensionValidator(allowed_extensions=['xls', 'xlsx', 'pdf', 'pptx'])],
                                     blank=True, null=True)
    company_bio = models.TextField(max_length=500, verbose_name='Company Bio', blank=True, null=True)
    ceo_bio = models.TextField(max_length=500, verbose_name='CEO Bio', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)


class Mandate(models.Model):
    """ Model to upload Mandate """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    investment_sought = models.ManyToManyField(InvestmentOffered, verbose_name='Type of investment sought')
    fund_size = models.ManyToManyField(ValuationFundTicket, verbose_name='Required minimum company or fund size ($USm)')
    size_ticket_total = models.ManyToManyField(ValuationFundTicket, verbose_name='Desired ticket size',
                                               related_name='mandate_size_ticket')
    percentage_company = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='% of company/fund can purchase/hold (min - max)')
    #
    # geography = models.ForeignKey(Geography, on_delete=models.SET_NULL, null=True)
    country = models.ManyToManyField(Country)
    #
    # sector = models.ForeignKey(Sector,on_delete=models.SET_NULL, verbose_name='Sector', blank=True, null=True)
    sub_sector = models.ManyToManyField(SubSector, verbose_name='Sub Sector')
    yield_select = models.ForeignKey(Yield, on_delete=models.CASCADE, verbose_name='Yield', null=True)
    #
    growth_expectation_year1 = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Minimum earnings growth required (%, FY1)')
    growth_expectation_year2 = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Minimum earnings growth required (%, FY2)')
    growth_expectation_year3 = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Minimum earnings growth required (%, FY3)')
    class_select = models.ManyToManyField(Class, verbose_name='Asset class')
    series_stage = models.ManyToManyField(SeriesStage, verbose_name='Series/stage of investment sought')
    investor_required = models.ForeignKey(InvestorSpecial, on_delete=models.CASCADE, verbose_name='Lead Investor required in place', null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)
