# Generated by Django 4.2.17 on 2024-12-16 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_phonenumber_entered_otp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonenumber',
            name='otp',
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='otp_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
