# Generated by Django 2.0.5 on 2018-06-26 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_comments_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
    ]