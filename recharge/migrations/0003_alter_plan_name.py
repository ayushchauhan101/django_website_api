# Generated by Django 4.1.4 on 2022-12-19 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recharge', '0002_alter_plan_validity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
