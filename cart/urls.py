from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('<int:product_id>/POST', views.createpost, name='createpost'),
    path('check_signup', views.check_signup, name='check_signup'),
    path('signup', views.render_signup, name='signup'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('', views.landing, name='landing'),
    path('clothing', views.clothing, name='clothing'),
    path('shoes', views.shoes, name='shoes'),
    path('equipment', views.equipment, name='equipment'),
    path('search', views.search, name='search')

]
