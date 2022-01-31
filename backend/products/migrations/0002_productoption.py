# Generated by Django 3.2.9 on 2022-01-31 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=100, verbose_name='사이즈')),
                ('color', models.CharField(max_length=100, verbose_name='색상')),
                ('stock_count', models.PositiveIntegerField(verbose_name='재고')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'db_table': 'product_option',
            },
        ),
    ]