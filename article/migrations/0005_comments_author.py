# Generated by Django 2.0.5 on 2018-06-26 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20180626_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
