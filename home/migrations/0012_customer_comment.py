# Generated by Django 3.2 on 2021-04-30 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_customer_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='comment',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
