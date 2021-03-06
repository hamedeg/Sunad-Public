# Generated by Django 3.2 on 2021-04-29 10:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import home.models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssn', models.CharField(max_length=14)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('gender', models.CharField(choices=[('Male', 'ذكر'), ('Female', 'أنثي')], max_length=6)),
                ('help_type', multiselectfield.db.fields.MultiSelectField(choices=[('Money', 'مال'), ('Food', 'طعام'), ('Medicine', 'دواء')], max_length=19)),
                ('partner_alive', models.CharField(choices=[('Yes', 'نعم'), ('No', 'لا'), ('Single', 'غير متزوج')], max_length=6)),
                ('number_children', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(0)])),
                ('number_brother', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='Customer_Attachments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachments', models.ImageField(upload_to=home.models.customer_img)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.customer')),
            ],
            options={
                'verbose_name_plural': 'Customer_Attachments',
            },
        ),
    ]
