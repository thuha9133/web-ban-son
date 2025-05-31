
from django.shortcuts import render, get_object_or_404, redirect
from .models import SanPham, TaiKhoan, KhachHang
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages


def trang_chu(request):
    san_pham_list = SanPham.objects.all()
    tai_khoan_list = TaiKhoan.objects.all()
    khach_hang_list = KhachHang.objects.all()

    context = {
        'san_pham_list': san_pham_list,
        'tai_khoan_list': tai_khoan_list,
        'khach_hang_list': khach_hang_list,
    }
    return render(request, 'quantri/trang_chu.html', context)

def them_san_pham(request):
    if request.method == 'POST':
        ten = request.POST['ten']
        mo_ta = request.POST['mo_ta']
        gia = request.POST['gia']
        so_luong = request.POST['so_luong']
        hinh_anh = request.FILES.get('hinh_anh')

        SanPham.objects.create(
            ten_san_pham=ten,
            mo_ta=mo_ta,
            gia=gia,
            so_luong=so_luong,
            hinh_anh=hinh_anh
        )
        return redirect('trang_chu')
    return render(request, 'quantri/them_san_pham.html')

def sua_san_pham(request, id):
    san_pham = get_object_or_404(SanPham, id=id)
    if request.method == 'POST':
        san_pham.ten_san_pham = request.POST['ten']
        san_pham.mo_ta = request.POST['mo_ta']
        san_pham.gia = request.POST['gia']
        san_pham.so_luong = request.POST['so_luong']
        # Nếu người dùng có upload hình mới, thì cập nhật
        if 'hinh_anh' in request.FILES:
            san_pham.hinh_anh = request.FILES['hinh_anh']

        san_pham.save()
        return redirect('trang_chu')
    return render(request, 'quantri/sua_san_pham.html', {'sp': san_pham})

def xoa_san_pham(request, id):
    san_pham = get_object_or_404(SanPham, id=id)
    san_pham.delete()
    return redirect('trang_chu')

def them_taikhoan(request):
    if request.method == 'POST':
        tenTK = request.POST.get('tenTK')
        matKhau = request.POST.get('matKhau')
        hoTen = request.POST.get('hoTen')
        email = request.POST.get('email')
        if tenTK and matKhau and hoTen and email:
            TaiKhoan.objects.create(
                tenTK=tenTK,
                matKhau=matKhau,
                hoTen=hoTen,
                email=email
            )
            messages.success(request, 'Thêm tài khoản thành công!')
            return redirect('trang_chu')
        else:
            messages.error(request, 'Vui lòng nhập đầy đủ thông tin!')
    return render(request, 'quantri/them_taikhoan.html')

def sua_taikhoan(request, id):
    tk = get_object_or_404(TaiKhoan, id=id)
    if request.method == 'POST':
        tk.tenTK = request.POST.get('tenTK')
        tk.matKhau = request.POST.get('matKhau')
        tk.hoTen = request.POST.get('hoTen')
        tk.email = request.POST.get('email')
        if tk.tenTK and tk.matKhau and tk.hoTen and tk.email:
            tk.save()
            messages.success(request, 'Cập nhật tài khoản thành công!')
            return redirect('trang_chu')
        else:
            messages.error(request, 'Vui lòng nhập đầy đủ thông tin!')
    return render(request, 'quantri/sua_taikhoan.html', {'taikhoan': tk})

def xoa_taikhoan(request, id):
    taikhoan = get_object_or_404(TaiKhoan, id=id)
    taikhoan.delete()
    return redirect('trang_chu')

# Thêm khách hàng
def them_khachhang(request):
    if request.method == 'POST':
        ten_khach = request.POST.get('ten_khach')
        email = request.POST.get('email')
        so_dien_thoai = request.POST.get('so_dien_thoai')
        dia_chi = request.POST.get('dia_chi')
        if ten_khach and email and so_dien_thoai and dia_chi:
            KhachHang.objects.create(
                ten_khach=ten_khach,
                email=email,
                so_dien_thoai=so_dien_thoai,
                dia_chi=dia_chi
            )
            messages.success(request, 'Thêm khách hàng thành công!')
            return redirect('trang_chu')
        else:
            messages.error(request, 'Vui lòng nhập đầy đủ thông tin!')
    return render(request, 'quantri/them_khachhang.html')

# Sửa khách hàng
def sua_khachhang(request, id):
    kh = get_object_or_404(KhachHang, id=id)
    if request.method == 'POST':
        kh.ten_khach = request.POST.get('ten_khach')
        kh.email = request.POST.get('email')
        kh.so_dien_thoai = request.POST.get('so_dien_thoai')
        kh.dia_chi = request.POST.get('dia_chi')
        if kh.ten_khach and kh.email and kh.so_dien_thoai and kh.dia_chi:
            kh.save()
            messages.success(request, 'Cập nhật khách hàng thành công!')
            return redirect('trang_chu')
        else:
            messages.error(request, 'Vui lòng nhập đầy đủ thông tin!')
    return render(request, 'quantri/sua_khachhang.html', {'khachhang': kh})

def xoa_khachhang(request, id):
    khachhang = get_object_or_404(KhachHang, id=id)
    khachhang.delete()
    return redirect('trang_chu')