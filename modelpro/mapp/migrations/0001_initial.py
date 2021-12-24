# Generated by Django 3.2 on 2021-12-20 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=254)),
                ('dept', models.CharField(max_length=50)),
                ('salary', models.BigIntegerField()),
                ('Address', models.TextField()),
            ],
        ),
    ]