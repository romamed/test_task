# Generated by Django 2.1.2 on 2019-02-13 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
                ('issue_date', models.DateField()),
                ('type', models.CharField(choices=[('P', 'Passport'), ('S', 'Student ID'), ('B', 'Birth Certificate')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('phone', models.CharField(max_length=11)),
                ('startday', models.DateField()),
                ('endday', models.DateField()),
                ('group', models.CharField(max_length=10)),
                ('university', models.CharField(max_length=20)),
            ],
        ),
    ]