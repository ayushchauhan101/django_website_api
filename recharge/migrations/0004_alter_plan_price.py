# Generated by Django 4.1.4 on 2022-12-19 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recharge', '0003_alter_plan_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
