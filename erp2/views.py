from django.shortcuts import render, redirect
from .models import ProductModel
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    user = request.user.is_authenticated
    if user:
        return render(request, 'erp/index.html')
    else:
        return redirect('/sign-in')
@login_required
def inbound(request):
    if request.method == 'GET':
        return render(request, 'erp/inbound_create.html')
    elif request.method == 'POST':
        product_code = request.POST.get('product_code', '')
        product_name = request.POST.get('product_name', '')
        product_descr = request.POST.get('product_description', '')
        product_price = request.POST.get('product_price', '')
        product_sizes = request.POST.get('product_sizes', '')
        product_quantity = request.POST.get('product_quantity', '')
        if product_code=='' or product_name=='' or product_price=='' or product_quantity=='':
            return render('erp/inbound_create.html',{'error': '제품코드, 이름, 가격, 수량은 필수칸입니다.'})
        else:
            ProductModel.objects.create_product(product_code=product_code, product_name=product_name, product_descr=product_descr,
                                                product_price=product_price,product_sizes=product_sizes,product_quantity=product_quantity)

            return redirect('/inbound')


@login_required
def inventory(request):
    if request.method == 'GET':

        return render(request, 'erp/inventory.html')
    else:
        return redirect('/sign-in')