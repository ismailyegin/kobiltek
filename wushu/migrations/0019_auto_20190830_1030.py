# Generated by Django 2.2.1 on 2019-08-30 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wushu', '0018_auto_20190830_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communication',
            name='address',
            field=models.TextField(default=0, verbose_name='Adres'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='phoneNumber',
            field=models.CharField(default=0, max_length=120),
        ),
        migrations.AlterField(
            model_name='communication',
            name='phoneNumber2',
            field=models.CharField(default=0, max_length=120),
        ),
        migrations.AlterField(
            model_name='communication',
            name='postalCode',
            field=models.CharField(default=0, max_length=120),
        ),
    ]