# Generated by Django 3.1.5 on 2021-03-21 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0006_auto_20210321_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.DecimalField(decimal_places=2, max_digits=2, null=True),
        ),
    ]
