# Generated by Django 3.2.1 on 2021-06-25 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anomaly', '0005_auto_20210625_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectionparam',
            name='file',
            field=models.JSONField(default=dict),
        ),
    ]