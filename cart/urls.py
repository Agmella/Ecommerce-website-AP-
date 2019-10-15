from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('<int:product_id>/POST', views.createpost, name='createpost'),
    path('checklogin', views.checklogin, name='checklogin'),
    path('login', views.render_login, name='login')
]
