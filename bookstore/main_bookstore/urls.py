from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .views import (
    BookCardView,
    CategoryDetailView,
    ShopView,
    CartView,
    AddToCartView,
    HomeView,
    DeleteFromCartView,
    ChangeQTYView,
    CheckoutView,
    MakeOrderView,
    LoginView,
    RegistrationView,
    ProfileView,
    BaseSpecView,
    CreateNewCategory,
    CreateNewFeature
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop', ShopView.as_view(), name='shop'),
    path('cart/', CartView.as_view(), name='cart'),
    path('about', views.about, name='aboutUs'),
    path('lk/', ProfileView.as_view(), name='lk'),
    path('book_card/<str:slug>', BookCardView.as_view(), name='book_card'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('add-to-cart/<str:slug>', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:slug>', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty/<str:slug>', ChangeQTYView.as_view(), name='change_qty'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('make-order/', MakeOrderView.as_view(), name='make_order'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page="/"), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('product_specs/', BaseSpecView.as_view(), name='base-spec'),
    path('product_specs/new-category', CreateNewCategory.as_view(), name='new-category'),
    path('product_specs/new-feature', CreateNewFeature.as_view(), name='new-feature'),
]
