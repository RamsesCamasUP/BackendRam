# Generated by Django 3.1.2 on 2020-11-02 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0003_auto_20201101_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='modified',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]