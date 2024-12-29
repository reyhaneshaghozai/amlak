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
    budget = models.DecimalField(max_digits=255, decimal_places=2, verbose_name="بودجه")
    area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="متراژ", null=True, blank=True)
    bedrooms = models.PositiveSmallIntegerField(verbose_name="تعداد اتاق خواب", null=True, blank=True)
    amenities = models.TextField(max_length=255, null=True, verbose_name="امکانات")
    description = models.TextField(null=True, blank=True, verbose_name="توضیحات")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان ثبت درخواست")

    def __str__(self):
        return f"{self.full_name} - {self.property_type}"
    class Meta:
        verbose_name = 'درخواست خرید ملک'
    
class Rental_Property(models.Model):
        PROPERTY_CHOICES = [
        ('Apartment', 'اپارتمان'),
        ('commercial', 'تجاری'),
        ('villa', 'ویلا'),
    ]
        location_type = models.CharField(max_length=20,choices=PROPERTY_CHOICES,verbose_name='موقعیت ملک شما')
        area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='متراژ')
        deposit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='پول پیش')
        rent = models.DecimalField(max_digits=10,decimal_places=2, verbose_name='مبلغ اجاره')
        commission = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='حق کمیسیون')
        bedrooms = models.PositiveSmallIntegerField(verbose_name="تعداد اتاق خواب", null=True, blank=True)
        amenities = models.TextField(max_length=255, null=True, verbose_name="امکانات")

        def __str__(self):
            return f"{self.get_location_type_display()} - {self.area} m²"
        class Meta:
            verbose_name = 'ملک برای اجاره'
class RentalPropertyRequest(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')  # ترکیب نام و نام خانوادگی
    phone_number = models.CharField(max_length=15, verbose_name='شماره تماس')
    city_and_neighborhood = models.CharField(max_length=200, verbose_name='شهر و محله')
    min_area = models.PositiveIntegerField(verbose_name='حداقل متراژ')
    max_area = models.PositiveIntegerField(verbose_name='حداکثر متراژ')
    min_deposit = models.PositiveIntegerField(verbose_name='حداقل پول پیش')
    min_rent = models.PositiveIntegerField(verbose_name='حداقل پول اجاره')
    family_members = models.PositiveIntegerField(verbose_name='تعداد افراد خانواده')
    bedrooms = models.PositiveSmallIntegerField(verbose_name="تعداد اتاق خواب", null=True, blank=True)

    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = 'درخواست اجاره ملک'
    
     