# Generated by Django 4.0.1 on 2022-01-13 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_address_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='region',
            field=models.CharField(choices=[('Namangan', 'Namangan'), ('Samarqand', 'Samarqand'), ('Andijon', 'Andijon'), ('Qashqadaryo', 'Qashqadaryo'), ('Toshkent', 'Toshkent:'), ('Surxondaryo', 'Surxondaryo'), ('Xorazm', 'Xorazm'), ('Navoi', 'Navoi')], default='empty', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50, null=True),
        ),
    ]
