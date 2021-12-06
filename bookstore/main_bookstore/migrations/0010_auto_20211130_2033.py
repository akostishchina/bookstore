# Generated by Django 3.2.9 on 2021-11-30 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_bookstore', '0009_productfeatures_productfeaturevalidators'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_name', models.CharField(max_length=100, verbose_name='Имя характеристики')),
                ('feature_filter_name', models.CharField(max_length=50, verbose_name='Имя для фильтра')),
                ('unit', models.CharField(blank=True, max_length=50, null=True, verbose_name='Единица измерения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_bookstore.category', verbose_name='Категория')),
            ],
            options={
                'unique_together': {('category', 'feature_name', 'feature_filter_name')},
            },
        ),
        migrations.CreateModel(
            name='FeatureValidator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_feature_value', models.CharField(max_length=100, verbose_name='Валидное значение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_bookstore.category', verbose_name='Категория')),
                ('feature_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_bookstore.categoryfeature', verbose_name='Ключ характеристики')),
            ],
        ),
        migrations.RemoveField(
            model_name='productfeatures',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productfeatures',
            name='feature_key',
        ),
        migrations.RemoveField(
            model_name='productfeatures',
            name='feature_name',
        ),
        migrations.RemoveField(
            model_name='productfeatures',
            name='filter_measure',
        ),
        migrations.RemoveField(
            model_name='productfeatures',
            name='filter_type',
        ),
        migrations.RemoveField(
            model_name='productfeatures',
            name='postfix_for_value',
        ),
        migrations.RemoveField(
            model_name='productfeatures',
            name='use_in_filter',
        ),
        migrations.AddField(
            model_name='productfeatures',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_bookstore.product', verbose_name='Товар'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productfeatures',
            name='value',
            field=models.CharField(default=1, max_length=255, verbose_name='Значение'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ProductFeatureValidators',
        ),
        migrations.AddField(
            model_name='productfeatures',
            name='feature',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_bookstore.categoryfeature', verbose_name='Характеристика'),
            preserve_default=False,
        ),
    ]
