# Generated by Django 4.2.17 on 2024-12-28 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rental_property_alter_propertyrequest_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental_property',
            name='amenities',
            field=models.TextField(max_length=255, null=True, verbose_name='امکانات'),
        ),
        migrations.AddField(
            model_name='rental_property',
            name='bedrooms',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='تعداد اتاق خواب'),
        ),
    ]
