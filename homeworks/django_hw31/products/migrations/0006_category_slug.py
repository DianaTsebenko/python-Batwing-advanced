# Generated by Django 3.1.1 on 2022-08-30 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20220826_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=100, null=True),
        ),
    ]