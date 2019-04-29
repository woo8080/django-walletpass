# Generated by Django 2.2 on 2019-04-29 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_type_identifier', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=50)),
                ('authentication_token', models.CharField(max_length=50)),
                ('data', models.FileField(upload_to='passes')),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'unique_together': {('pass_type_identifier', 'serial_number')},
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_library_identifier', models.CharField(max_length=50)),
                ('push_token', models.CharField(max_length=50)),
                ('pazz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_passbook.Pass')),
            ],
        ),
    ]
