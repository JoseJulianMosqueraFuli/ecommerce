# Generated by Django 4.2.4 on 2023-09-13 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='active',
            field=models.BooleanField(),
        ),
    ]
