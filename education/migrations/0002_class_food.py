# Generated by Django 2.2 on 2019-04-16 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.TextField(blank=True, max_length=18500, null=True, verbose_name='Yemek Menüsü')),
                ('food_date', models.DateField(verbose_name='Yemek Tarihi')),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Sınıf Adı')),
                ('education_year', models.CharField(choices=[('2018-2019', '2018-2019'), ('2019-2020', '2019-2020')], default='2018-2019', max_length=128, verbose_name='Eğitim Yılı')),
                ('creationDate', models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')),
                ('modificationDate', models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')),
                ('students', models.ManyToManyField(to='education.Student', verbose_name='Öğrenci')),
            ],
        ),
    ]
