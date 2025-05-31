from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Trang chủ
    path('gioithieu/', views.gioithieu, name='gioithieu'), # Giới thiệu
    path('sanpham/', views.sanpham, name='sanpham'),    
    path('romand23/', views.romand23, name='romand23'),
    path('lienhe/', views.lienhe, name='lienhe'), # Liên hệ
    path('register/', views.register, name='register'), # Đăng ký
    path('login/', views.login, name='login'), # Đăng nhập
    path('profile/', views.profile, name='profile'), # Thông tin người dùng
    path('cart/', views.cart, name='cart'),
    path('them-vao-gio/<int:id>/', views.them_vao_gio, name='them_vao_gio'),
    path('thanhtoan/', views.thanhtoan, name='thanhtoan'),

]
