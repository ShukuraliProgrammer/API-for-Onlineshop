# Generated by Django 4.0.1 on 2022-01-17 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_category_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='level',
            field=models.CharField(choices=[('3', '3'), ('1', '1'), ('2', '2')], max_length=200, null=True),
        ),
    ]
