# Generated by Django 2.2.6 on 2019-10-16 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='report_title',
            field=models.IntegerField(choices=[(0, 'Report_1'), (1, 'Report_2'), (2, 'Report_3')], default=-1),
        ),
    ]
