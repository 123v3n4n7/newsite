# Generated by Django 2.0.5 on 2018-06-21 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Text', models.TextField()),
                ('Date', models.DateTimeField()),
                ('Likes', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]
