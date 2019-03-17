# Generated by Django 2.1.7 on 2019-03-17 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsQuantityOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Goods')),
            ],
        ),
        migrations.RemoveField(
            model_name='goodsquatityorder',
            name='goods',
        ),
        migrations.RemoveField(
            model_name='goodsquatityorder',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='change_key',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='order',
            name='goods',
            field=models.ManyToManyField(related_name='orders', through='core.GoodsQuantityOrder', to='core.Goods'),
        ),
        migrations.DeleteModel(
            name='GoodsQuatityOrder',
        ),
        migrations.AddField(
            model_name='goodsquantityorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_quantity', to='core.Order'),
        ),
    ]