# Generated by Django 2.1.1 on 2018-09-11 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cattegorys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField(max_length=10, null=True)),
                ('food', models.CharField(blank=True, max_length=50, null=True)),
                ('buy_place', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
