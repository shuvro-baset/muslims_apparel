# Generated by Django 3.2.4 on 2021-06-29 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0003_alter_product_updated_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('UPCOMING PRODUCTS', 'UPCOMING PRODUCTS'), ('ORGANIC FOOD', 'ORGANIC FOOD'), ('MOST DEMANDABLE PRODUCTS', 'MOST DEMANDABLE PRODUCTS'), ('KHILMAR', 'KHILMAR'), ('JILBAB', 'JILBAB'), ('ABAYA/BORKA', 'ABAYA/BORKA'), ('LINEN', 'LINEN'), ('COTTON', 'COTTON'), ('CAPE', 'CAPE'), ('NIQAB', 'NIQAB'), ('HAND GLOVES & SOCKS', 'HAND GLOVES & SOCKS'), ('SUNNAH ITEM', 'SUNNAH ITEM')], default=('UPCOMING PRODUCTS', 'UPCOMING PRODUCTS'), max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='pro_img',
            field=models.ImageField(help_text='<h2 style="color: #008CBA;">Images size must be height: 1200px and width: 1486px format.</h2>', upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='img',
            field=models.ImageField(help_text='<h2 style="color: #008CBA;">Images size must be height: 1200px and width: 1486px format.</h2>', upload_to='slider_images'),
        ),
    ]