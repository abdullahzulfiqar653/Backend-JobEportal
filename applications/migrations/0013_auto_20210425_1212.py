# Generated by Django 3.2 on 2021-04-25 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0012_auto_20210423_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualifiedcv',
            name='file',
            field=models.FileField(upload_to='files'),
        ),
        migrations.AlterField(
            model_name='unqualifiedcv',
            name='file',
            field=models.FileField(upload_to='files'),
        ),
    ]
