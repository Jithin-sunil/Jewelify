# Generated by Django 5.1.4 on 2025-01-06 05:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0001_initial'),
        ('Shop', '0005_alter_tbl_stock_stock_date'),
        ('User', '0003_tbl_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_datetime', models.CharField(max_length=30)),
                ('rating_value', models.CharField(max_length=30)),
                ('rating_content', models.CharField(max_length=30)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.tbl_product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
