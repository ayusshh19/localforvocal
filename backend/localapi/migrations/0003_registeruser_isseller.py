# Generated by Django 4.1 on 2023-02-13 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localapi', '0002_alter_addproduct_prodimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeruser',
            name='isseller',
            field=models.BooleanField(default=True, max_length=10),
        ),
    ]