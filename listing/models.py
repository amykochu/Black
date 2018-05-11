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


class Listing(models.Model):

    WIDGET_6_CHOICES = (
        (1, '0-6 months'),
        (2, '6-12 months'),
        (3, '12-24 months'),
        (4, '24 months +'),
    )

    WIDGET_7_CHOICES = (
        (1, '0-20'),
        (2, '20-50'),
        (3, '50-100'),
        (4, '100-500'),
        (5, '500-2000'),
    )

    WIDGET_10_CHOICES = (
        (1, '1-4'),
        (2, '4-8'),
        (3, '8 +')
    )

    WIDGET_12_CHOICES = (
        (1, 'Year 1'),
        (2, 'Year 2'),
        (3, 'Year 3')
    )

    WIDGET_15_CHOICES = (
        (1, 'YES'),
        (2, 'NO')
    )

    WIDGET_16_CHOICES = (
        (1, 'Option A'),
        (2, 'Option B')
    )

    WIDGET_18_CHOICES = (
        (1, 'YES'),
        (2, 'NO')
    )

    widget1 = models.CharField(max_length=500)
    widget2 = models.CharField(max_length=500)
    widget3 = models.CharField(max_length=500)
    widget4 = models.CharField(max_length=500)
    widget5 = models.CharField(max_length=500)
    widget6 = models.IntegerField(choices=WIDGET_6_CHOICES)
    widget7 = models.IntegerField(choices=WIDGET_7_CHOICES)
    widget8 = models.ManyToManyField(Widget8)
    widget9 = models.ManyToManyField(Widget9)
    widget10 = models.IntegerField(choices=WIDGET_10_CHOICES)
    widget11 = models.CharField(max_length=500)
    widget12 = models.IntegerField(choices=WIDGET_12_CHOICES)
    widget13 = models.ManyToManyField(Widget13)
    widget14 = models.ManyToManyField(Widget14)
    widget15 = models.IntegerField(choices=WIDGET_15_CHOICES)
    widget16 = models.IntegerField(choices=WIDGET_16_CHOICES)
    widget17 = models.ManyToManyField(Widget17)
    widget18 = models.IntegerField(choices=WIDGET_18_CHOICES)
    widget19 = models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.widget1

    class Meta:

        verbose_name = 'Listing'
        verbose_name_plural = 'Listings'
