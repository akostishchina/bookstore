from PIL import Image

from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

"""
class BooksAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            '<span style="color:red; font-size:14px;">Загружайте изображения с минимальным разрешением {}x{}</span>'.format(
                *Product.MIN_RESOLUTION
            )
        )

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = Product.MIN_RESOLUTION
        max_height, max_width = Product.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Размер изображения не должен превышать 3 Мб')
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Загруженное изображение меньше минимального разрешения')
        if img.height > max_height or img.width > max_width:
            raise ValidationError('Загруженное изображение больше максимального разрешения')
        return image


class BooksAdmin(admin.ModelAdmin):

    form = BooksAdminForm
"""

admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
#admin.site.register(ProductFeatures)
#admin.site.register(FeatureValidator)
#admin.site.register(CategoryFeature)

