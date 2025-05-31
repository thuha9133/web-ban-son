from django.urls import path
from . import views

urlpatterns = [
    path('', views.trang_chu, name='trang_chu'),
    path('sanpham/them/', views.them_san_pham, name='them_san_pham'),
    path('sanpham/sua/<int:id>/', views.sua_san_pham, name='sua_san_pham'),
    path('sanpham/xoa/<int:id>/', views.xoa_san_pham, name='xoa_san_pham'),
    path('taikhoan/them/', views.them_taikhoan, name='them_taikhoan'),
    path('taikhoan/sua/<int:id>/', views.sua_taikhoan, name='sua_taikhoan'),
    path('taikhoan/xoa/<int:id>/', views.xoa_taikhoan, name='xoa_taikhoan'),
    path('khachhang/them/', views.them_khachhang, name='them_khachhang'),
    path('khachhang/sua/<int:id>/', views.sua_khachhang, name='sua_khachhang'),
    path('khachhang/xoa/<int:id>/', views.xoa_khachhang, name='xoa_khachhang'),
]
