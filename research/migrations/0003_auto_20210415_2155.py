# Generated by Django 3.1.6 on 2021-04-15 16:25

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0002_auto_20210414_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=100, null=True),
        ),
    ]
