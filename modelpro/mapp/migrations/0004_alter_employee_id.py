# Generated by Django 3.2 on 2021-12-20 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0003_alter_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
