# Generated by Django 2.2.1 on 2019-05-02 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_activecourier'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
