# Generated by Django 5.1.4 on 2025-01-04 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_tbl_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_stock',
            name='stock_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
