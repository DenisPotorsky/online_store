# Generated by Django 4.2.9 on 2024-01-28 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_goods_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Goods',
            new_name='Good',
        ),
    ]
