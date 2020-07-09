# Generated by Django 2.2.2 on 2020-07-09 15:58

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='cell_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Contact cell phone number', max_length=128, region=None, unique=True),
        ),
    ]
