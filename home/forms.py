from django import forms
from .models import PropertyRequest,Rental_Property,RentalPropertyRequest

class PropertyRequestForm(forms.ModelForm):
    AMENITY_CHOICES = [
        ('parking', 'پارکینگ'),
        ('elevator', 'آسانسور'),
        ('storage', 'انباری'),
        ('garden', 'باغ'),
        ]
    amenities = forms.MultipleChoiceField(choices=AMENITY_CHOICES,widget=forms.CheckboxSelectMultiple,label="امکانات")
    class Meta:

        model = PropertyRequest
        fields = ['property_type', 'full_name', 'contact_number', 'province', 'city', 'budget', 'bedrooms', 'area', 'description','amenities']


    def __init__(self, *args, **kwargs):
        super(PropertyRequestForm, self).__init__(*args, **kwargs)
        # اجباری بودن تمام فیلدها
        for field in self.fields.values():
            field.required = True

class RentalPropertyForm(forms.ModelForm):
        AMENITY_CHOICES = [
        ('parking', 'پارکینگ'),
        ('elevator', 'آسانسور'),
        ('storage', 'انباری'),
        ('garden', 'باغ'),
    ]

        amenities = forms.MultipleChoiceField(
            choices=AMENITY_CHOICES,
            widget=forms.CheckboxSelectMultiple,
            label="امکانات"
        )
        class Meta:
            model = Rental_Property
            fields = ['location_type', 'area', 'deposit', 'rent', 'commission','bedrooms', 'amenities']

class RentalPropertyRequestForm(forms.ModelForm):
    class Meta:
        model = RentalPropertyRequest
        fields = ['full_name', 'phone_number', 'city_and_neighborhood', 'min_area', 'max_area', 'min_deposit', 'min_rent', 'family_members','bedrooms']
        labels = {
            'full_name': 'نام و نام خانوادگی',
            'phone_number': 'شماره تماس',
            'city_and_neighborhood': 'شهر و محله',
            'min_area': 'حداقل متراژ',
            'max_area': 'حداکثر متراژ',
            'min_deposit': 'حداقل پول پیش',
            'min_rent': 'حداقل پول اجاره',
            'family_members': 'تعداد افراد خانواده',
            'bedrooms' : 'تعداد اتاق خواب ',
        }
