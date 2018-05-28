from django.db import models


class Widget8(models.Model):

    widget_choice = models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.widget_choice


class Widget9(models.Model):

    widget_choice = models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.widget_choice


class Widget13(models.Model):

    widget_choice = models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.widget_choice


class Widget14(models.Model):

    widget_choice = models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.widget_choice


class Widget17(models.Model):

    widget_choice = models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.widget_choice


INVESTMENT_OFFERED_CHOICES = (
    (1, 'Private'),
    (2, 'Listed'),
    (3, 'Fund'),
    (4, 'Direct'),
    (5, 'Co-Invest')
)

VALUATION_FUND_TICKET_CHOICES = (
    (1, '0-20'),
    (2, '20-50'),
    (3, '50-100'),
    (4, '100-500'),
    (5, '500-2000'),
    (6, '2000+')
)

YIELD_CHOICES = (
    (1, '1-4'),
    (2, '4-8'),
    (3, '8 +')
)

CLASS_CHOICES = (
    (1, 'Debt'),
    (2, 'Equity'),
    (3, 'Private Equity'),
    (4, 'Listed Equity'),
    (5, 'Mezz'),
    (6, 'Real Estate')
)

SERIES_STAGE_CHOICES = (
    (1, 'A'),
    (2, 'B'),
    (3, 'C'),
    (4, 'Growth'),
    (5, 'Pre-IPO'),
    (6, 'Construction')
)

INVESTOR_AND_SPECIAL_CHOICES = (
    (1, 'YES'),
    (2, 'NO')
)


class Opportunity(models.Model):
    """ Model for opportunity upload """

    EST_PAYBACK_CHOICES = (
        (1, '0-6 months'),
        (2, '6-12 months'),
        (3, '12-24 months'),
        (4, '24 months +')
    )

    OFFER_CHOICES = (
        (1, 'Broad process'),
        (2, 'Privately offered')
    )

    FINANCIAL_CHOICES = (
        (1, 'USD'),
        (2, 'AUD'),
        (3, 'EUR'),
        (4, 'GBP')
    )

    company_description = models.CharField(max_length=500, verbose_name='Company / Fund description')
    opportunity_created = models.CharField(max_length=500, verbose_name='What makes this opportunity unique? '
                                                                        'How will value be created/unlocked?')
    selling_by = models.CharField(max_length=500, verbose_name='Who is selling? Why?')
    competitors = models.CharField(max_length=500, verbose_name='Major competitors')
    valuation = models.IntegerField(choices=VALUATION_FUND_TICKET_CHOICES,
                                    verbose_name='Valuation - metrics and rationale')
    amount_invested = models.DecimalField(max_digits=30, decimal_places=4,
                                          verbose_name='Amount invested to date ($USm)')
    ownership_structure = models.FloatField(max_length=3, verbose_name='Ownership structure (%)')
    ebitda = models.FloatField(verbose_name='Company EBITDA ($USm)')
    break_even_year = models.FloatField(verbose_name='Break-even year')
    est_payback = models.IntegerField(choices=EST_PAYBACK_CHOICES, verbose_name='Est. payback on raise')
    size_ticket_total = models.IntegerField(choices=VALUATION_FUND_TICKET_CHOICES,
                                            verbose_name='Size ticket total available')
    #
    geography = models.CharField(max_length=500, verbose_name='Geography')
    #
    sector = models.CharField(max_length=500, verbose_name='Sector')
    yield_select = models.IntegerField(choices=YIELD_CHOICES, verbose_name='Yield')
    return_estimate = models.FloatField(verbose_name='Return estimate (3-yr) (%)')
    #
    growth_expectation = models.CharField(max_length=500, verbose_name='Earnings growth expectation (%)')
    class_select = models.IntegerField(choices=CLASS_CHOICES, verbose_name='Class')
    series_stage = models.IntegerField(choices=SERIES_STAGE_CHOICES, verbose_name='Series/stage')
    investor_required = models.IntegerField(choices=INVESTOR_AND_SPECIAL_CHOICES,
                                            verbose_name='Lead Investor required in place')
    amount_lead_partner = models.FloatField(verbose_name='Amount injected by Lead Partner')
    amount_other_partner = models.FloatField(verbose_name='Amount injected by Other Partners')
    amount_weraise = models.FloatField(verbose_name='Amount available for WeRaise')
    investment_offered = models.IntegerField(choices=INVESTMENT_OFFERED_CHOICES,
                                             verbose_name='Type of investment offered')
    offer = models.IntegerField(choices=OFFER_CHOICES, verbose_name='Offer')
    special_situation = models.IntegerField(choices= INVESTOR_AND_SPECIAL_CHOICES, verbose_name='Special situation')
    financials = models.IntegerField(choices=FINANCIAL_CHOICES, verbose_name='Financials')
    #
    Revenue = models.CharField(max_length=500, verbose_name='Revenue')
    estimated_irr = models.FloatField(verbose_name='Estimated IRR')
    exit_timing = models.CharField(max_length=500, verbose_name='Expected exit timing')
    use_of_funds = models.CharField(max_length=500, verbose_name='Use of funds')
    deadline_commitment = models.FloatField(verbose_name='Deadline for formal commitment')
    deadline_legal = models.FloatField(verbose_name='Deadline for execution of legal docs')
    proposed_process = models.CharField(max_length=500, verbose_name='Proposed process')
    proposed_exit = models.CharField(max_length=500, verbose_name='Proposed exit options')
    # 3
    financial_statements = models.FileField(upload_to='documents/',
                                            verbose_name='Do you have 3 years audited financial statements available?')
    financial_model = models.FileField(upload_to='documents/', verbose_name='Do you have a financial model?')
    investor_deck = models.FileField(upload_to='documents/', verbose_name='Do you have an investor deck?')
    company_bio = models.TextField(max_length=500, verbose_name='Company Bio')
    ceo_bio = models.TextField(max_length=500, verbose_name='CEO Bio')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pk


class Mandate(models.Model):
    """ Model to upload Mandate """

    investment_sought = models.IntegerField(choices=INVESTMENT_OFFERED_CHOICES,
                                            verbose_name='Type of investment sought')
    fund_size = models.IntegerField(choices=VALUATION_FUND_TICKET_CHOICES, verbose_name='Required company or fund size')
    size_ticket_total = models.IntegerField(choices=VALUATION_FUND_TICKET_CHOICES,
                                            verbose_name='Desired ticket size')
    percentage_company = models.FloatField(verbose_name='% of company (min - max)')
    #
    geography = models.CharField(max_length=500, verbose_name='Geography')
    #
    sector = models.CharField(max_length=500, verbose_name='Sector')
    yield_select = models.IntegerField(choices=YIELD_CHOICES, verbose_name='Yield')
    #
    growth_required = models.CharField(max_length=500, verbose_name='Earnings growth required (%)')
    class_select = models.IntegerField(choices=CLASS_CHOICES, verbose_name='Class')
    series_stage = models.IntegerField(choices=SERIES_STAGE_CHOICES, verbose_name='Series/stage')
    investor_required = models.IntegerField(choices=INVESTOR_AND_SPECIAL_CHOICES,
                                            verbose_name='Lead Investor required in place')
