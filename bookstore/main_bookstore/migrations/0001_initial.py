# Generated by Django 3.2.9 on 2021-11-13 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_products', models.PositiveIntegerField(default=0)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая цена')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('task', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('qty', models.PositiveIntegerField(default=1)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая цена')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_products', to='main_bookstore.cart', verbose_name='Корзина')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_bookstore.customer', verbose_name='Пользователь')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_bookstore.customer', verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='related_cart', to='main_bookstore.CartProduct'),
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название книги')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('author', models.CharField(max_length=255, verbose_name='Автор книги')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('limit_age', models.CharField(max_length=255, verbose_name='Ограничение по возрасту')),
                ('qty_page', models.DecimalField(decimal_places=0, max_digits=5, verbose_name='Кол-во страниц')),
                ('publishing_house', models.CharField(max_length=255, verbose_name='Издательство')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_bookstore.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
