# Generated by Django 3.0.3 on 2020-05-05 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent2app', '0005_auto_20200505_1017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliverymodel',
            old_name='cus_addr',
            new_name='d_address',
        ),
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
