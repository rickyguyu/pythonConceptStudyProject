# Generated by Django 4.0.3 on 2022-04-11 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_alter_businessinfo_hblfiles_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessinfo',
            name='dp_invoice',
            field=models.FileField(blank=True, db_column='DP_Invoice', null=True, upload_to='DPIs-%Y%m/'),
        ),
    ]
