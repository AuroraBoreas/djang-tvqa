from django.db import models
from django.db.models.base import Model
from django.utils import timezone
import datetime
year = datetime.datetime.today().year
month = datetime.datetime.today().month

class PMod(models.Model):
    name           = models.CharField(max_length=5)
    part_number    = models.CharField(max_length=9)
    date_created   = models.DateTimeField(default=timezone.now)
    year_quotated  = models.IntegerField(default=year, blank=False, null=False)
    month_quotated = models.IntegerField(default=month, blank=False, null=False)
    unit_price     = models.DecimalField(decimal_places=2, max_digits=100)
    BOM_registered = models.BooleanField(default=False)

    def __repr__(self):
        return 'PMod {}'.format(self.name)