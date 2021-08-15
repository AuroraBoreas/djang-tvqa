from django.core.checks import messages
from django.shortcuts import redirect, render, get_list_or_404
from django.contrib import messages
from django.db.models.functions import Upper
from django.db.models import Value
from .form import PModRegisterForm, PMod

from django.http.request import HttpRequest
from typing import NewType, Type, TypeVar
Request = NewType('Request', HttpRequest)
T = TypeVar('T', None, int)

def pmod_bom_create_view(request:Request, *args, **kwargs):
    if request.method == 'POST':
        form = PModRegisterForm(request.POST)
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
                print(pmods)
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

def try_parse(s:str)->T:
    try:
        rv = int(s)
    except ValueError:
        rv = None
    return rv

def pmod_bom_list_view(request:Request, *args, **kwargs):
    if request.method == 'POST':
        name           = request.POST.get('pmodname') or None
        part_number    = request.POST.get('partnumber') or None
        year_quotated  = try_parse(request.POST.get('bomyear'))
        month_quotated = try_parse(request.POST.get('bommonth'))
        BOM_registered = True if request.POST.get('bomregistered') == 'on' else False
        search_dict    = {'BOM_registered':BOM_registered} # multi-conditions
        if name:
            search_dict['name'] = name.upper()
        if part_number:
            search_dict['part_number'] = part_number.upper()
        if year_quotated:
            search_dict['year_quotated'] = year_quotated
        if month_quotated:
            search_dict['month_quotated'] = month_quotated
        pmods = PMod.objects.filter(**search_dict)
        context = {
            'pmods': pmods
        }
        return render(request, template_name='bom_list.html', context=context)
    else:
        return render(request, template_name='bom_list.html')

def pmod_bom_update_view(request:Request, *args, **kwargs):
    pass