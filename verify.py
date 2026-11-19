import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','funding_dashboard.settings')
import django
django.setup()
from django.test import Client
from opportunities.models import Opportunity
from django.test.utils import setup_test_environment
setup_test_environment()
c=Client()
r=c.get('/')
assert r.status_code==200 and r.context['total']==386
assert len(r.context['page'])==15
r=c.get('/',{'q':'4Di Capital'})
assert r.status_code==200 and r.context['matched']>0
assert all('4di' in x.financing_organisation_name.lower() for x in r.context['page'])
r=c.get('/',{'investment_instrument':'Equity','financial_sector_type':'Private sector'})
assert r.context['matched']>0
assert all(x.investment_instrument=='Equity' and x.financial_sector_type=='Private sector' for x in r.context['page'])
assert c.get('/',{'q':'zzzznotfoundzzzz'}).context['matched']==0
assert c.get('/',{'page':'invalid'}).status_code==200
assert c.get('/',{'page':999}).status_code==200
for item in Opportunity.objects.all():
    assert c.get(f'/opportunities/{item.pk}/').status_code==200
    assert not any(x in str(item.investment_opportunity_information) for x in ['\u00e2\u20ac','\u00ef\u00bf\u00bd'])
assert c.get('/opportunities/99999/').status_code==404
print('Verified overview, search, combined filters, empty state, pagination, and all 386 detail pages.')
