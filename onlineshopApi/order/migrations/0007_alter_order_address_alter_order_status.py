# Generated by Django 4.0.1 on 2022-01-18 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0043_alter_address_region'),
        ('order', '0006_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_address', to='accounts.address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('Received', 'Received'), ('Shipped', 'Shipped'), ('In Progress', 'In Progress'), ('Scheduled', 'Scheduled')], max_length=100, null=True),
        ),
    ]
