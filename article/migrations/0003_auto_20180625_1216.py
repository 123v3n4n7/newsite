# Generated by Django 2.0.5 on 2018-06-25 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20180621_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_text',
            field=models.TextField(verbose_name=''),
        ),
    ]
