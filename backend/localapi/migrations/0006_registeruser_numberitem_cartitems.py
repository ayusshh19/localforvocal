# Generated by Django 4.1 on 2023-02-13 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localapi', '0005_registeruser_registertime'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeruser',
            name='numberitem',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='cartitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addtime', models.DateTimeField(auto_now=True)),
                ('prodid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localapi.addproduct')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localapi.registeruser')),
            ],
        ),
    ]
