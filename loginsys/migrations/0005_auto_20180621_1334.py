# Generated by Django 2.0.5 on 2018-06-21 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0004_auto_20180620_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
    ]
