# Generated by Django 3.0 on 2021-05-19 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210505_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]