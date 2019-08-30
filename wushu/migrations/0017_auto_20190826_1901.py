# Generated by Django 2.2.1 on 2019-08-26 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wushu', '0016_sportclubuser_sportclub'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='belts',
            field=models.ManyToManyField(to='wushu.Level'),
        ),
        migrations.AlterField(
            model_name='level',
            name='branch',
            field=models.CharField(choices=[('TAOLU', 'TAOLU'), ('SANDA', 'SANDA'), ('WUSHU', 'WUSHU')], default=3, max_length=128, verbose_name='Branş'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='level',
            name='levelType',
            field=models.CharField(choices=[('VISA', 'VISA'), ('GRADE', 'GRADE'), ('BELT', 'BELT')], max_length=128, verbose_name='Leveller'),
        ),
    ]
