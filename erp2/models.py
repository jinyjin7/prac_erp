from django.db import models
from django.contrib.auth.models import AbstractUser


# 상품(상품 코드, 상품 이름, 상품 설명, 상품 가격, 사이즈 필드)
class ProductModel(models.Model):
    class Meta:
        app_label = 'myapp'
        db_table = "my_product"

    product_code = models.CharField(max_length=256, default='')
    product_name = models.CharField(max_length=50, default='')
    product_descr = models.CharField(max_length=50, default='')
    product_price = models.DecimalField(max_digits=10, decimal_places=1)
    product_sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    product_size = models.CharField(choices=product_sizes, max_length=1)
    product_quantity = models.IntegerField(default=0)

# choices 매개변수는 Django 모델 필드에서 사용하는 매개변수 중 하나로
# 해당 필드에서 선택 가능한 옵션을 지정하는 역할을 합니다.
# 변수를 통해 튜플 리스트를 받으면 첫번째 요소는 실제 DB에 저장되는 값이 되고,
# 두번째 요소는 사용자가 볼 수 있는 레이블(옵션의 이름)이 됩니다.

# def __str__(self):
#     return self.code
#
# def save(self, *args, **kwargs):
#     if not self.pk:  # 객체가 생성될 때
#         self.inventory_quantity = 0
#     super().save(*args, **kwargs)


# 입고(상품, 수량, 입고 날짜, 금액 필드를 작성)
class Inbound(ProductModel):
    class Meta:
        app_label = 'erp2'
    inbound_quantity = models.IntegerField()
    inbound_date = models.DateTimeField(auto_now_add=True)

class Inventory(ProductModel):
    class Meta:
        app_label = 'erp2'

