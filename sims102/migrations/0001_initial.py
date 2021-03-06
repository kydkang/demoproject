# Generated by Django 2.2.6 on 2019-10-29 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('commons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index101',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_one', models.IntegerField(verbose_name='FT')),
                ('data_two', models.IntegerField(verbose_name='DT')),
                ('data_three', models.IntegerField(verbose_name='PT')),
                ('calculated_value', models.DecimalField(blank=True, decimal_places=2, max_digits=7, verbose_name='NPFD')),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commons.Description')),
            ],
            options={
                'ordering': ['id'],
                'permissions': [('index101_contributor', 'index101_contributor'), ('index101_validator', 'index101_validator')],
            },
        ),
    ]
