# Generated by Django 2.2.6 on 2019-10-23 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0004_pizza_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='status',
            new_name='available',
        ),
    ]