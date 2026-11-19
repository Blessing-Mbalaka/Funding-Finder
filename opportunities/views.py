from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Opportunity

FILTERS = [('financial_sector_type','Financial sector'),('investment_instrument','Investment instrument'),('financing_organisation_type','Provider type'),('organisation_seeking_funding','Applicant type'),('eip_initiatives_result','EIP initiative')]

def dashboard(request):
    source = Opportunity.objects.all()
    records = source
    query = request.GET.get('q','').strip()
    if query:
        condition = Q()
        for field in ['financing_organisation_name','fund_name','funding_focus','eligibility_criteria','investment_opportunity_information']:
            condition |= Q(**{field+'__icontains':query})
        records = records.filter(condition)
    filters = []
    for field,label in FILTERS:
        value = request.GET.get(field,'')
        choices = sorted(set(source.exclude(**{field:''}).values_list(field,flat=True)),key=str.casefold)
        filters.append(dict(field=field,label=label,value=value,choices=choices))
        if value:
            records = records.filter(**{field:value})
    params = request.GET.copy()
    params.pop('page',None)
    return render(request,'opportunities/dashboard.html',dict(page=Paginator(records,15).get_page(request.GET.get('page')),filters=filters,query=query,params=params.urlencode(),total=source.count(),providers=source.values('financing_organisation_name').distinct().count(),linked=source.exclude(weblink='').count(),matched=records.count()))

def detail(request,pk):
    item = get_object_or_404(Opportunity,pk=pk)
    fields = [(f.verbose_name.capitalize(),getattr(item,f.name)) for f in item._meta.fields if f.name not in ('id','source_number','financing_organisation_name','fund_name')]
    return render(request,'opportunities/detail.html',dict(item=item,fields=fields))
