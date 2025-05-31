from django.db import models

# Create your models here.

# Sản phẩm mỹ phẩm
class SanPham(models.Model):
    ten_san_pham = models.CharField(max_length=200, verbose_name="Tên sản phẩm")
    mo_ta = models.TextField(verbose_name="Mô tả sản phẩm")
    gia = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Giá bán")
    so_luong = models.PositiveIntegerField(verbose_name="Số lượng trong kho")
    hinh_anh = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name="Hình ảnh")
    def __str__(self):
        return self.ten_san_pham
    
#Tài khoản
class  TaiKhoan(models.Model):
    tenTK =models.CharField(max_length=30)
    matKhau=models.CharField(max_length=50)
    hoTen=models.CharField(max_length=35)
    email=models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.tenTK
    
# Khách hàng
class KhachHang(models.Model):
    ten_khach = models.CharField(max_length=100, verbose_name="Tên khách hàng")
    email = models.EmailField(unique=True, verbose_name="Email")
    so_dien_thoai = models.CharField(max_length=15, verbose_name="Số điện thoại")
    dia_chi = models.TextField(verbose_name="Địa chỉ")

    def __str__(self):
        return self.ten_khach

# Đơn hàng
class DonHang(models.Model):
    khach_hang = models.ForeignKey(KhachHang, on_delete=models.CASCADE, verbose_name="Khách hàng")
    ngay_dat = models.DateTimeField(auto_now_add=True, verbose_name="Ngày đặt hàng")
    ghi_chu = models.TextField(blank=True, verbose_name="Ghi chú")

    def __str__(self):
        return f"Đơn hàng #{self.id} - {self.khach_hang.ten_khach}"

# Chi tiết đơn hàng
class ChiTietDonHang(models.Model):
    don_hang = models.ForeignKey(DonHang, on_delete=models.CASCADE, related_name="chi_tiet", verbose_name="Đơn hàng")
    san_pham = models.ForeignKey(SanPham, on_delete=models.CASCADE, verbose_name="Sản phẩm")
    so_luong = models.PositiveIntegerField(verbose_name="Số lượng")

    def __str__(self):
        return f"{self.so_luong} x {self.san_pham.ten_san_pham}"
