# Generated by Django 3.2 on 2021-04-29 11:22

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_customerattachments_customer_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='help_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Money', 'مال'), ('Food', 'طعام'), ('Medicine', 'دواء')], default='', max_length=19),
        ),
    ]