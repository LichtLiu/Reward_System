# Generated by Django 2.2.6 on 2019-10-31 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_situation', '0003_auto_20191031_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='point',
            field=models.IntegerField(default=0),
        ),
    ]