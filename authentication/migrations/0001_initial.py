# Generated by Django 4.2.17 on 2024-12-19 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('otp_code', models.CharField(blank=True, max_length=6, null=True)),
                ('entered_otp', models.CharField(blank=True, max_length=6, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('password2', models.CharField(max_length=8)),
                ('password1', models.CharField(max_length=8)),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
