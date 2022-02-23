# Generated by Django 4.0.1 on 2022-01-24 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_product_label_alter_category_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='level',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
