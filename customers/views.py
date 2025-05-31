from django.shortcuts import render, redirect
from quantri.models import SanPham 
from django.shortcuts import render, redirect, get_object_or_404


def sanpham(request):
    danh_sach_san_pham = SanPham.objects.all()
    return render(request, 'customers/sanpham.html', {
        'danh_sach_san_pham': danh_sach_san_pham
    })

def index(request):
    return render(request, 'customers/index.html')

def gioithieu(request):
    return render(request, 'customers/gioithieu.html')

def chitiet(request, id):
    return render(request, 'customers/chitiet.html')

def romand23(request):
    return render(request, 'customers/romand23.html')
def cart(request):
    return render(request, 'customers/cart.html')

def lienhe(request):
    return render(request, 'customers/lienhe.html')

def register(request):
    return render(request, 'customers/register.html')




def login(request):
    if request.method == 'POST':
        # (Ở đây bạn có thể thêm logic kiểm tra tài khoản nếu cần)
        return redirect('index')  # chuyển hướng đến trang chủ sau khi đăng nhập
    return render(request, 'customers/login.html')


def profile(request):
    return render(request, 'customers/profile.html')
def them_vao_gio(request, id):
    product = get_object_or_404(SanPham, id=id)
    cart = request.session.get('cart', {})

    if str(product.id) in cart:
        cart[str(product.id)]['quantity'] += 1
    else:
        cart[str(product.id)] = {'quantity': 1}

    request.session['cart'] = cart
    return redirect('sanpham')

def thanhtoan(request):
    cart = request.session.get('cart', {})

    products = []
    total = 0

    for product_id, item in cart.items():
        try:
            product = SanPham.objects.get(id=product_id)
            quantity = item['quantity']
            subtotal = product.gia * quantity
            total += subtotal
            products.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal
            })
        except SanPham.DoesNotExist:
            continue

    return render(request, 'customers/thanhtoan.html', {
        'products': products,
        'total': total
    })


