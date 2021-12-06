from django.views.generic.detail import SingleObjectMixin
from django.views.generic import View
from .models import Category, Cart, Customer

"""
class CategoryDetailMixin(SingleObjectMixin):
    
    CATEGORY_SLUG2PRODUCT_MODEL = {
        'foreign_classic': Books,
        'childish': Books,
        'graphic_novel': Books,
        'romance_novel': Books,
        'russian_classic': Books
    }

    def get_context_data(self, **kwargs):
        if isinstance(self.get_object(), Category):
            model = self.CATEGORY_SLUG2PRODUCT_MODEL[self.get_object().slug]
            context = super().get_context_data(**kwargs)
            context['categories'] = Category.objects.get_categories_for_right_sidebar()
            context['category_products'] = model.objects.all()
            return context
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.get_categories_for_right_sidebar()
        return context
"""


class CartMixin(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:       #если пользователь авторизован
            customer = Customer.objects.filter(user=request.user).first()    #ищем его
            if not customer: #если не нашли юзера, то можем его создать
                customer = Customer.objects.create(
                    user=request.user
                )
            cart = Cart.objects.filter(owner=customer, in_order=False).first()   #ищем корзину, которая существует и не находится в заказе
            if not cart:
                cart = Cart.objects.create(owner=customer)

        else:
            cart = Cart.objects.filter(for_anonymous_user=True).first()
            if not cart:
                cart = Cart.objects.create(for_anonymous_user=True)
        self.cart = cart

        return super().dispatch(request, *args, **kwargs)


