# Generated by Django 3.2 on 2021-04-29 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_customer_attachments_customerattachments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerattachments',
            name='customer_key',
            field=models.CharField(max_length=200),
        ),
    ]
