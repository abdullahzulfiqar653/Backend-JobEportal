# Generated by Django 3.2 on 2021-04-23 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0005_auto_20210423_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unqualifiedcv',
            name='degree_date_1',
            field=models.CharField(default='', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='unqualifiedcv',
            name='degree_date_2',
            field=models.CharField(default='', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='unqualifiedcv',
            name='degree_date_3',
            field=models.CharField(default='', max_length=256, null=True),
        ),
    ]