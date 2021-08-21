from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.db.models.functions import Upper
from django.db.models import Value
import csv
from .form import PModRegisterForm, PMod, PModSearchForm

from django.http.request import HttpRequest
from typing import NewType
Request = NewType('Request', HttpRequest)

def pmod_bom_create_view(request:Request, *args, **kwargs):
    if request.method == 'POST':
        form = PModRegisterForm(request.POST or None)
        if form.is_valid():
            name           = form.cleaned_data.get('name')
            part_number    = form.cleaned_data.get('part_number')
            date_created   = form.cleaned_data.get('date_created')
            year_quotated  = form.cleaned_data.get('year_quotated')
            month_quotated = form.cleaned_data.get('month_quotated')
            unit_price     = form.cleaned_data.get('unit_price')
            BOM_registered = form.cleaned_data.get('BOM_registered')
            try:
                pmods = PMod.objects.filter(name__iexact=name, 
                                        part_number__iexact=part_number,
                                        year_quotated__iexact=year_quotated,
                                        month_quotated__iexact=month_quotated,
                                        # BOM_registered__iexact=BOM_registered,
                )
                # print(pmods)
            except PMod.DoesNotExist:
                pmods = None
            if pmods.exists():
                messages.warning(request, 'PMod existed already!')
                return redirect('pmods:pmod_bom_create')
            else:
                pmod_new = PMod(name=Upper(Value(name)), 
                                part_number=Upper(Value(part_number)),
                                date_created=Upper(Value(date_created)),
                                year_quotated=Upper(Value(year_quotated)),
                                month_quotated=Upper(Value(month_quotated)),
                                unit_price=Upper(Value(unit_price)),
                                BOM_registered=Upper(Value(BOM_registered))
                )
                pmod_new.save()
                pmod_new.refresh_from_db()
                messages.success(request, "PMod created successfully!")
                return redirect('pmods:pmod_bom_create')
    else:
        form = PModRegisterForm()
    context = {
        'form': form,
    }
    return render(request, template_name='bom_create.html', context=context)

def pmod_bom_list_view(request:Request, *args, **kwargs):
    form = PModSearchForm(request.POST or None)
    qs = PMod.objects.all()
    context = {
        'form'  : form,
        'pmods' : qs
    }
    if request.method == 'POST':
        form = PModSearchForm(request.POST or None) 
        search_dict = {}
        if form['name'].value():
            search_dict['name'] = form['name'].value()
        if form['date_created'].value():
            search_dict['date_created'] = form['date_created'].value()
        if form['year_quotated'].value():
            search_dict['year_quotated'] = form['year_quotated'].value()
        if form['month_quotated'].value():
            search_dict['month_quotated'] = form['month_quotated'].value()
        if form['BOM_registered'].value():
            search_dict['BOM_registered'] = form['BOM_registered'].value()
        # print(search_dict)
        qs = PMod.objects.filter(**search_dict)
        # print(qs)
        context = {
            'form' : form,
            'pmods': qs
        }
        if form['export_to_csv'].value():
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="pmod_buyback.csv"'
            writer = csv.writer(response)
            writer.writerow([
                'name',
                'part_number',
                'date_created',
                'year_quotated',
                'month_quotated',
                'unit_price',
                'BOM_registered',
            ])            
            for row in qs.values_list():
                writer.writerow(row)
            return response
        else:
            return render(request, template_name='bom_list.html', context=context)
    return render(request, template_name='bom_list.html', context=context)

def pmod_bom_update_view(request:Request, *args, **kwargs):
    pass