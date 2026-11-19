from django.db import models
from urllib.parse import urlsplit

class Opportunity(models.Model):
    source_number = models.IntegerField(unique=True)
    organisation_seeking_funding = models.TextField(blank=True)
    financial_sector_type = models.TextField(blank=True)
    investment_instrument = models.TextField(blank=True)
    financing_organisation_type = models.TextField(blank=True)
    eip_initiatives_search = models.TextField(blank=True)
    financing_organisation_name = models.TextField(blank=True)
    fund_name = models.TextField(blank=True)
    funding_focus = models.TextField(blank=True)
    eip_initiatives_result = models.TextField(blank=True)
    finance_threshold = models.TextField(blank=True)
    eligibility_criteria = models.TextField(blank=True)
    weblink = models.TextField(blank=True)
    contact_details = models.TextField(blank=True)
    investment_opportunity_information = models.TextField(blank=True)

    class Meta:
        ordering = ['financing_organisation_name', 'source_number']
    def __str__(self):
        return self.financing_organisation_name
    @property
    def website_url(self):
        value = self.weblink.strip()
        if not value:
            return ''
        if '://' not in value:
            value = 'https://' + value
        parsed = urlsplit(value)
        return value if parsed.scheme in ('https', 'http') and parsed.netloc and not any(c.isspace() for c in value) else ''
