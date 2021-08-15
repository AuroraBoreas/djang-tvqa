from django.forms import ModelForm
from .models import PMod

class PModRegisterForm(ModelForm):
    class Meta:
        model = PMod
        fields = [
            'name',
            'part_number',
            # 'date_created',
            'year_quotated',
            'month_quotated',
            # 'unit_price',
            'BOM_registered',
        ]