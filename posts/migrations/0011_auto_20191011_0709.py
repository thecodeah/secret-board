# Generated by Django 2.1.7 on 2019-10-11 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20191006_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='approved',
            new_name='hidden',
        ),
    ]
