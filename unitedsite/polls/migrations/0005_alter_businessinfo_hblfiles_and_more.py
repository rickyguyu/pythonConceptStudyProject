# Generated by Django 4.0.3 on 2022-04-11 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_businessinfo_hblfiles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessinfo',
            name='hblfiles',
            field=models.FileField(blank=True, db_column='HBLFiles', null=True, upload_to='hbls/'),
        ),
        migrations.AlterField(
            model_name='businessinfo',
            name='mblfile',
            field=models.FileField(blank=True, db_column='MBLFile', null=True, upload_to='mbls/'),
        ),
    ]
