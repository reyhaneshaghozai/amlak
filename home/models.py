from django.db import models

class PropertyRequest(models.Model):
    PROPERTY_CHOICES = [
        ('buy', 'خرید یک ملک'),
        ('sell', 'فروش یک ملک'),
        ('rent', 'اجاره یک ملک'),
    ]
    property_type = models.CharField(max_length=10, choices=PROPERTY_CHOICES, default='buy', verbose_name="نوع ملک")
    full_name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    contact_number = models.CharField(max_length=12, verbose_name="شماره تماس")
    province = models.CharField(max_length=50, verbose_name="استان")
    city = models.CharField(max_length=50, verbose_name="شهر/بخش")
    budget = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="بودجه")
    area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="متراژ", null=True, blank=True)
    amenities = models.TextField(max_length=255, verbose_name="امکانات")
    bedrooms = models.PositiveSmallIntegerField(verbose_name="تعداد اتاق خواب", null=True, blank=True)
    description = models.TextField(null=True, blank=True, verbose_name="توضیحات")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان ثبت درخواست")


    def __str__(self):
        return f"{self.full_name} - {self.property_type}"
