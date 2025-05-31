from django.contrib import admin

# Register your models here.

from .models import  SanPham, KhachHang, DonHang, ChiTietDonHang, TaiKhoan
@admin.register(TaiKhoan)
class TaiKhoanAdmin(admin.ModelAdmin):
    list_display = ['tenTK', 'matKhau', 'hoTen', 'email']

@admin.register(SanPham)
class SanPhamAdmin(admin.ModelAdmin):
    list_display = ['id', 'ten_san_pham','mo_ta', 'gia', 'so_luong']

@admin.register(KhachHang)
class KhachHangAdmin(admin.ModelAdmin):
    list_display = ['id', 'ten_khach', 'email', 'so_dien_thoai']

class ChiTietDonHangInline(admin.TabularInline):
    model = ChiTietDonHang
    extra = 1

@admin.register(DonHang)
class DonHangAdmin(admin.ModelAdmin):
    list_display = ['id', 'khach_hang', 'ngay_dat']
    inlines = [ChiTietDonHangInline]
