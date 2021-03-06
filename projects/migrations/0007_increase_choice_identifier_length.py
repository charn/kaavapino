# Generated by Django 2.0 on 2018-01-06 13:06

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_add_fields_to_attributes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributevaluechoice',
            name='identifier',
            field=models.CharField(db_index=True, max_length=150, validators=[django.core.validators.RegexValidator(re.compile('^[\\w]+\\Z'), "Enter a valid 'identifier' consisting of Unicode letters, numbers or underscores.", 'invalid')], verbose_name='identifier'),
        ),
    ]
