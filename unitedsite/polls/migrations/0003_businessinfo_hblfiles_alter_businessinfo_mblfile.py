# Generated by Django 4.0.3 on 2022-04-11 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_businessinfo_mblfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessinfo',
            name='hblfiles',
            field=models.FileField(blank=True, db_column='HBLFiles', max_length='150', null=True, upload_to='upload/mbl/'),
        ),
        migrations.AlterField(
            model_name='businessinfo',
            name='mblfile',
            field=models.FileField(blank=True, db_column='MBLFile', max_length='150', null=True, upload_to='upload/mbl/'),
        ),
    ]