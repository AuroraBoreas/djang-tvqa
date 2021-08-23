# Generated by Django 3.2.6 on 2021-08-21 13:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmods', '0003_alter_pmod_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pmod',
            name='export_to_csv',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pmod',
            name='name',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('[a-zA-Z]{2,3}[0-9]{2,3}', 'Only PMod name allowed(i.e: AG85)')]),
        ),
        migrations.AlterField(
            model_name='pmod',
            name='part_number',
            field=models.CharField(max_length=9, validators=[django.core.validators.RegexValidator('[a-zA-Z]{1}[0-9]{7}[a-zA-Z]{1}', 'Only PMod part number allowed(i.e: A5030081A)')]),
        ),
    ]