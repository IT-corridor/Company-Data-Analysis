from __future__ import unicode_literals

from django.db import models

class CompanyData(models.Model):
    companyid = models.CharField(max_length=50)
    report_date = models.DateField()
    dc = models.CharField(max_length=50, null=True, blank=True)
    ca_acct = models.CharField(max_length=50, null=True, blank=True)
    main_acct = models.CharField(max_length=50, null=True, blank=True)
    customer_name = models.CharField(max_length=50, null=True, blank=True)
    ca_formulary = models.CharField(max_length=50, null=True, blank=True)
    mus_formulary = models.CharField(max_length=50, null=True, blank=True)
    alternate_items = models.CharField(max_length=50, null=True, blank=True)
    utilization = models.CharField(max_length=50, null=True, blank=True)
    refill_line_utilization = models.CharField(max_length=50, null=True, blank=True)
    ca_doses_dispensed = models.CharField(max_length=50, null=True, blank=True)
    non_ca_doses_dispensed = models.CharField(max_length=50, null=True, blank=True)
    total_doses_dispenses = models.CharField(max_length=50, null=True, blank=True)
    total_refills = models.CharField(max_length=50, null=True, blank=True)
    ca_lines_refilled = models.CharField(max_length=50, null=True, blank=True)
    non_ca_lines_refilled = models.CharField(max_length=50, null=True, blank=True)
    ca_vend_to_refill_ratio = models.CharField(max_length=50, null=True, blank=True)
    non_ca_vend_to_refill_ratio = models.CharField(max_length=50, null=True, blank=True)
    total_vend_refill_ratio = models.CharField(max_length=50, null=True, blank=True)
    non_ca_stock_outs = models.CharField(max_length=50, null=True, blank=True)
    ca_stock_outs = models.CharField(max_length=50, null=True, blank=True)
    total_stock_outs = models.CharField(max_length=50, null=True, blank=True)
    total_stock_outs_per_100_dispenses = models.CharField(max_length=50, null=True, blank=True)
    totalmedstation = models.CharField(max_length=50, null=True, blank=True)
    blockedmedstation = models.CharField(max_length=50, null=True, blank=True)
    activemedstation = models.CharField(max_length=50, null=True, blank=True)
    ineligible_items = models.CharField(max_length=50, null=True, blank=True)
    ca_scan_qty = models.CharField(max_length=50, null=True, blank=True)
    ca_refill_qty = models.CharField(max_length=50, null=True, blank=True)
    ca_scan_rate = models.CharField(max_length=50, null=True, blank=True)
    non_ca_scan_qty = models.CharField(max_length=50, null=True, blank=True)
    non_ca_refill_qty = models.CharField(max_length=50, null=True, blank=True)
    non_ca_scan_rate = models.CharField(max_length=50, null=True, blank=True)
    total_scan_qty = models.CharField(max_length=50, null=True, blank=True)
    total_refill_qty = models.CharField(max_length=50, null=True, blank=True)
    totalscanrate = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.report_date, self.companyid)

    class Meta:
        verbose_name = 'Company Data'
        verbose_name_plural = 'Company Data'
