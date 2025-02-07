# Generated by Django 5.1.4 on 2025-01-09 07:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0001_initial'),
        ('User', '0024_delete_tbl_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_date', models.DateField(auto_now_add=True)),
                ('complaint_replay', models.CharField(max_length=30)),
                ('complaint_status', models.IntegerField(default=0)),
                ('complaint_file', models.FileField(upload_to='Assets/UserDocs/')),
                ('complaint_description', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
