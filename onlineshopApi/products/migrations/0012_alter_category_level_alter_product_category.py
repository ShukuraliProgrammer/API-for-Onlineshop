# Generated by Django 4.0.1 on 2022-01-17 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_category_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='level',
            field=models.CharField(choices=[('2', '2'), ('1', '1'), ('3', '3')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category'),
        ),
    ]
