# Generated by Django 2.1.7 on 2019-04-14 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190412_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveCourier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(max_length=128)),
                ('has_order', models.BooleanField()),
            ],
        ),
    ]
