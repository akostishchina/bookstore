# Generated by Django 3.2.9 on 2021-11-19 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_bookstore', '0002_cart_in_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.AlterField(
            model_name='cart',
            name='final_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Общая цена'),
        ),
    ]