# Generated by Django 4.1 on 2023-02-13 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localapi', '0003_registeruser_isseller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeruser',
            name='isseller',
            field=models.BooleanField(default=False, max_length=10),
        ),
    ]
