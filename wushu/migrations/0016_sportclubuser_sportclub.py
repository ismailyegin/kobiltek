# Generated by Django 2.2.1 on 2019-08-26 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wushu', '0015_sportclubuser_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportclubuser',
            name='sportClub',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='wushu.SportsClub', verbose_name='Spor Kulübü'),
            preserve_default=False,
        ),
    ]