# Generated by Django 3.1 on 2022-04-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Document', '0003_auto_20220406_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='cheque',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='driving',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='pancard',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='salaryslip',
            field=models.ImageField(upload_to='images'),
        ),
    ]