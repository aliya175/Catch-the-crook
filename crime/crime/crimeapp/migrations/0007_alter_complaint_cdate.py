# Generated by Django 4.0.3 on 2022-09-29 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimeapp', '0006_alter_wantedlist_wdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='cdate',
            field=models.DateField(auto_now=True),
        ),
    ]