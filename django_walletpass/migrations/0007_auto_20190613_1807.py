# Generated by Django 2.2 on 2019-06-13 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_walletpass', '0006_auto_20190613_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pass',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]