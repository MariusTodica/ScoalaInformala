# Generated by Django 4.0.4 on 2022-05-05 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='active',
            field=models.BooleanField(default=1),
        ),
    ]