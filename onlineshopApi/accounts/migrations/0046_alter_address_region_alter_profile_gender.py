# Generated by Django 4.0.1 on 2022-01-22 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0045_alter_address_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='region',
            field=models.CharField(choices=[('Jizzax', 'Jizzax'), ('Samarqand', 'Samarqand'), ('Andijon', 'Andijon'), ('Qashqadaryo', 'Qashqadaryo'), ('Xorazm', 'Xorazm'), ('Buxoro', 'Buxoro'), ('Surxondaryo', 'Surxondaryo'), ('Toshkent vil', 'Toshkent vil'), ('Navoi', 'Navoi'), ('Fargona', 'Fargona'), ('Toshkent', 'Toshkent:'), ('Namangan', 'Namangan')], default='empty', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=50, null=True),
        ),
    ]
