# Generated by Django 3.2 on 2021-04-29 11:25

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_customer_help_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='help_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Money', 'مال'), ('Food', 'طعام'), ('Medicine', 'دواء')], default='Money', max_length=19),
        ),
    ]
