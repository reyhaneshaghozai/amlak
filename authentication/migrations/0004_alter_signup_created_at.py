# Generated by Django 4.2.17 on 2024-12-19 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_signup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
