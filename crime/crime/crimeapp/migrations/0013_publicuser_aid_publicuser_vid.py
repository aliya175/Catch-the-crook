# Generated by Django 4.0.3 on 2022-11-03 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimeapp', '0012_missingpersonupdate_stname'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicuser',
            name='aid',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='publicuser',
            name='vid',
            field=models.CharField(max_length=100, null=True),
        ),
    ]