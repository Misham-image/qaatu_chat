# Generated by Django 4.2 on 2023-04-14 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daybook', '0003_alter_journels_invoice_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journels',
            old_name='Invoice_Number',
            new_name='InvoiceNum',
        ),
    ]
