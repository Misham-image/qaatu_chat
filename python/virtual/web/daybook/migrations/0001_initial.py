# Generated by Django 4.2 on 2023-04-14 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='journels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Products', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('Invoice_Number', models.CharField(max_length=500)),
                ('Date', models.DateField()),
            ],
        ),
    ]
