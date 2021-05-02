# Generated by Django 3.2 on 2021-05-02 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210502_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='courier',
            name='username',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='address',
            name='region',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_name',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_number',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='courier',
            name='email',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='courier',
            name='first_name',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='courier',
            name='last_name',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='courier',
            name='password',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='courier',
            name='phone_number',
            field=models.CharField(default='', max_length=256),
        ),
    ]
