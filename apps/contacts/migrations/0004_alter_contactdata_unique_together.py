# Generated by Django 4.2.4 on 2023-08-25 13:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0003_contactdatatype_message"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="contactdata",
            unique_together={("contact", "data_type")},
        ),
    ]
