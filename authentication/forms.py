from django import forms
from.models import Signup

class PhoneNumberForm(forms.Form):
    phone_number = forms.CharField(
        max_length=15,
        label="شماره تلفن",
        widget=forms.TextInput(attrs={'placeholder': 'مثال: 09121234567'}),
        required=True
    )

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not phone.isdigit() or len(phone) not in [10, 11]:
            raise forms.ValidationError("شماره تلفن معتبر نیست.")
        return phone

class SignupForm(forms.ModelForm):             
    class Meta:
        model = Signup
        fields = ['phone_number','email','password1','password2']
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }

    
