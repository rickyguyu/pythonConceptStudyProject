# Generated by Django 4.0.3 on 2022-04-09 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, max_length=20, null=True)),
                ('user_pwd', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
