# Generated by Django 2.2.5 on 2019-10-01 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('population', models.PositiveIntegerField(verbose_name='population')),
                ('tz', models.CharField(blank=True, max_length=50)),
                ('visits', models.PositiveIntegerField()),
                ('commonwealth', models.NullBooleanField()),
                ('flag', models.FileField(blank=True, upload_to='country/flags/')),
                ('continent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='record.Continent')),
            ],
            options={
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='full name')),
                ('friendly', models.BooleanField(default=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='record.Country')),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
    ]