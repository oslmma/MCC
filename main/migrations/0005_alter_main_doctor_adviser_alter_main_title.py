# Generated by Django 4.1.3 on 2022-11-27 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_main_rac_alter_main_ch123_alter_main_ch45_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='doctor_adviser',
            field=models.CharField(blank=True, max_length=125),
        ),
        migrations.AlterField(
            model_name='main',
            name='title',
            field=models.CharField(blank=True, max_length=125),
        ),
    ]