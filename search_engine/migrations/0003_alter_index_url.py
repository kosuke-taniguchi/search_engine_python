# Generated by Django 3.2.7 on 2021-10-02 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0002_auto_20211002_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='url',
            field=models.CharField(max_length=2048),
        ),
    ]