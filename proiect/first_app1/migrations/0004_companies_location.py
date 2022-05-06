# Generated by Django 4.0.4 on 2022-05-06 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
        ('first_app1', '0003_remove_companies_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='first_app.location'),
            preserve_default=False,
        ),
    ]