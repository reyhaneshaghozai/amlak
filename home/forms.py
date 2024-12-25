from django import forms
from .models import PropertyRequest

class PropertyRequestForm(forms.ModelForm):
    AMENITY_CHOICES = [
        ('parking', 'پارکینگ'),
        ('elevator', 'آسانسور'),
        ('storage', 'انباری'),
        ('garden', 'باغ'),
    ]
    
    amenities = forms.MultipleChoiceField(
        choices=AMENITY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    
    class Meta:
        model = PropertyRequest
        fields = ['property_type', 'full_name', 'contact_number', 'province', 'city', 'budget', 'area', 'bedrooms', 'description']

    def __init__(self, *args, **kwargs):
        super(PropertyRequestForm, self).__init__(*args, **kwargs)
        # اجباری بودن تمام فیلدها
        for field in self.fields.values():
            field.required = True
