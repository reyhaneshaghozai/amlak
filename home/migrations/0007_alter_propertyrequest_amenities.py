# Generated by Django 4.2.17 on 2024-12-29 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rentalpropertyrequest_alter_propertyrequest_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyrequest',
            name='amenities',
            field=models.CharField(choices=[('parking', 'پارکینگ'), ('elevator', 'آسانسور'), ('storage', 'انباری'), ('garden', 'باغ')], max_length=255, verbose_name='امکانات'),
        ),
    ]