from django.contrib import admin
from .models import Opportunity
@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('financing_organisation_name','fund_name','investment_instrument')
    search_fields = ('financing_organisation_name','fund_name')
    list_filter = ('financial_sector_type','investment_instrument')
admin.site.site_header = 'Funding Atlas administration'
