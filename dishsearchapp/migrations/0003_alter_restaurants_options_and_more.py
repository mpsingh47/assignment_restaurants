# Generated by Django 4.2.2 on 2023-06-28 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishsearchapp', '0002_restaurants_full_details_restaurants_items_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurants',
            options={'verbose_name_plural': 'Restaurants DB'},
        ),
        migrations.RenameField(
            model_name='restaurants',
            old_name='lat_lon',
            new_name='lat_long',
        ),
        migrations.AlterModelTable(
            name='restaurants',
            table='restaurants_db',
        ),
    ]
