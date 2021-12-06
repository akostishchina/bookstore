import sys
from PIL import Image

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from django.urls import reverse

User = get_user_model()


class MinResolutionErrorException(Exception):
    pass


class MaxResolutionErrorException(Exception):
    pass


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})
"""
    def get_fields_for_filter_in_template(self):
        return ProductFeatures.objects.filter(
            category=self,
            use_in_filter=True
        ).prefetch_related('category').value('feature_key', 'feature_measure', 'feature_name', 'filter_type')
"""


class Product(models.Model):

    MIN_RESOLUTION = (200, 200)
    MAX_RESOLUTION = (500, 500)
    MAX_IMAGE_SIZE = 3145728

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Название книги')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    author = models.CharField(max_length=255, verbose_name='Автор книги')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        image = self.image
        img = Image.open(image)
        min_height, min_width = self.MIN_RESOLUTION
        max_height, max_width = self.MAX_RESOLUTION
        if img.height < min_height or img.width < min_width:
            raise MinResolutionErrorException('Загруженное изображение меньше минимального разрешения')
        if img.height > max_height or img.width > max_width:
            raise MaxResolutionErrorException('Загруженное изображение больше максимального разрешения')
        super().save(*args, **kwargs)

    def get_model_name(self):
        return self.__class__.__name__.lower()

    def get_absolute_url(self):
        return reverse('book_card', kwargs={'slug': self.slug})


class CartProduct(models.Model):

    user = models.ForeignKey('Customer', verbose_name='Пользователь', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.product.title)

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.product.price
        super().save(*args, **kwargs)


class Cart(models.Model):

    owner = models.ForeignKey('Customer', null=True, verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name='Общая цена')
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20,verbose_name='Номер телефона', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
    orders = models.ManyToManyField('Order', related_name='related_customer', verbose_name='Заказы покупателя')

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)


class Order(models.Model):

    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'is_ready'
    STATUS_COMPLETED = 'completed'

    BUYING_TYPE_SELF = 'self'
    BUYING_TYPE_DELIVERY = 'delivery'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_IN_PROGRESS, 'Заказ в обработке'),
        (STATUS_READY, 'Заказ готов'),
        (STATUS_COMPLETED, 'Заказ выполнен')
    )

    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, 'Самовывоз'),
        (BUYING_TYPE_DELIVERY, 'Доставка')
    )

    customer = models.ForeignKey(Customer, verbose_name='Покупатель', related_name='related_orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=255, verbose_name='Отчество', null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=1024, verbose_name='Адрес', null=True, blank=True)
    status = models.CharField(
        max_length=100,
        verbose_name='Статус заказа',
        choices=STATUS_CHOICES,
        default=STATUS_NEW
    )
    buying_type = models.CharField(
        max_length=100,
        verbose_name='Тип заказа',
        choices=BUYING_TYPE_CHOICES,
        default=BUYING_TYPE_SELF
    )
    comment = models.TextField(verbose_name='Комментарий', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')
    order_date = models.DateField(verbose_name='Дата получения заказа', default=timezone.now)

    def __str__(self):
        return str(self.id)

"""
class CategoryFeature(models.Model):

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=100, verbose_name='Имя характеристики')
    feature_filter_name = models.CharField(max_length=50, verbose_name='Имя для фильтра')
    unit = models.CharField(max_length=50, verbose_name='Единица измерения', null=True, blank=True)

    class Meta:
        unique_together = ('category', 'feature_name', 'feature_filter_name')

    def __str__(self):
        return f"{self.category.name} | {self.feature_name}"


class FeatureValidator(models.Model):

    

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    feature_key = models.ForeignKey(CategoryFeature, verbose_name='Ключ характеристики', on_delete=models.CASCADE)
    valid_feature_value = models.CharField(max_length=100, verbose_name='Валидное значение')

    def __str__(self):
        return f"Категория \"{self.category.name}\" | " \
               f"Характеристика \"{self.feature_key.feature_name}\" | " \
               f"Валидное значение \"{self.valid_feature_value}\""


class ProductFeatures(models.Model):

        

        product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
        feature = models.ForeignKey(CategoryFeature, verbose_name='Характеристика', on_delete=models.CASCADE)
        value = models.CharField(max_length=255, verbose_name='Значение')

        def __str__(self):
            return f"Товар - {self.product.title} | " \
                   f"Характеристика - {self.feature.feature_name} | " \
                   f"Значение - {self.value}"
"""

