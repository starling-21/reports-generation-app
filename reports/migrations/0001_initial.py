# Generated by Django 2.2.5 on 2019-09-28 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_title', models.CharField(max_length=255)),
                ('position_tail', models.CharField(blank=True, max_length=255)),
                ('supervisor', models.BooleanField(blank=True, null=True)),
                ('temp_supervisor', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('to_name', models.CharField(blank=True, max_length=255, null=True)),
                ('for_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('parent_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reports.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='Serviceman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('to_first_name', models.CharField(max_length=255)),
                ('to_last_name', models.CharField(max_length=255)),
                ('for_first_name', models.CharField(max_length=255)),
                ('for_last_name', models.CharField(max_length=255)),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reports.Position')),
                ('rank', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reports.Rank')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reports.Unit')),
            ],
        ),
        migrations.AddField(
            model_name='position',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reports.Unit'),
        ),
    ]