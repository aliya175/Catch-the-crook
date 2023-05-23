# Generated by Django 4.0.3 on 2022-09-28 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comptitle', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('identification', models.CharField(max_length=100)),
                ('cdate', models.DateField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Criminal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('identification', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('optype', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Filerequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('receiver', models.CharField(max_length=100)),
                ('frequest', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firdate', models.DateField()),
                ('lawapplied', models.CharField(max_length=100)),
                ('cdate', models.DateField()),
                ('details', models.CharField(max_length=100)),
                ('cid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimeapp.complaint')),
                ('crid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimeapp.criminal')),
            ],
        ),
        migrations.CreateModel(
            name='Hearing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heardate', models.DateField()),
                ('updates', models.CharField(max_length=100)),
                ('firid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimeapp.fir')),
            ],
        ),
        migrations.CreateModel(
            name='Missingitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('identification', models.CharField(max_length=100)),
                ('datemissing', models.DateField()),
                ('placemissing', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Missingperson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('identification', models.CharField(max_length=100)),
                ('estheight', models.CharField(max_length=100)),
                ('estweight', models.CharField(max_length=100)),
                ('physic', models.CharField(max_length=100)),
                ('missdate', models.DateField()),
                ('missplace', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publicuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Wantedlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wdate', models.DateField()),
                ('crid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimeapp.criminal')),
            ],
        ),
        migrations.CreateModel(
            name='Punishment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('punishment', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('hid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimeapp.hearing')),
            ],
        ),
        migrations.CreateModel(
            name='Missingthingsupdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('udate', models.DateField()),
                ('updates', models.CharField(max_length=100)),
                ('mid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimeapp.missingitems')),
            ],
        ),
        migrations.CreateModel(
            name='Missingpersonupdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('udate', models.DateField()),
                ('updates', models.CharField(max_length=100)),
                ('mid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimeapp.missingperson')),
            ],
        ),
        migrations.AddField(
            model_name='missingperson',
            name='pid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimeapp.publicuser'),
        ),
        migrations.AddField(
            model_name='missingitems',
            name='pid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimeapp.publicuser'),
        ),
        migrations.AddField(
            model_name='missingitems',
            name='sid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimeapp.station'),
        ),
        migrations.CreateModel(
            name='Filee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='')),
                ('frid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimeapp.filerequest')),
            ],
        ),
        migrations.CreateModel(
            name='Complaintupdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('udate', models.DateField()),
                ('updates', models.CharField(max_length=100)),
                ('cid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimeapp.complaint')),
            ],
        ),
        migrations.AddField(
            model_name='complaint',
            name='pid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimeapp.publicuser'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='sid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimeapp.station'),
        ),
    ]