# Generated by Django 3.1.4 on 2021-01-30 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citymaps', '0002_auto_20201220_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='subtitle',
            field=models.TextField(blank=True, null=True),
        ),
    ]
