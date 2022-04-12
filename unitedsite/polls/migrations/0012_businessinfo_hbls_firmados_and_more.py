# Generated by Django 4.0.3 on 2022-04-12 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_businessinfo_dp_voucher_businessinfo_hp_voucher'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessinfo',
            name='hbls_firmados',
            field=models.FileField(blank=True, db_column='HBLs_Firmados', null=True, upload_to='HBLCFRMDs-%Y%m/'),
        ),
        migrations.AddField(
            model_name='businessinfo',
            name='income_invoice',
            field=models.FileField(blank=True, db_column='Income_Invoice', null=True, upload_to='INI-%Y%m/'),
        ),
        migrations.AddField(
            model_name='businessinfo',
            name='income_voucher',
            field=models.FileField(blank=True, db_column='Income_Voucher', null=True, upload_to='INVs-%Y%m/'),
        ),
    ]
