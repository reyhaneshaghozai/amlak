from django import forms
from.models import Signup,PhoneNumber

class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['phone_number','password']
        widgets = {
            'phone_number':forms.TextInput(attrs={'placeholder': 'مثال: 09121234567','class':'forms__form'}),
            'password':forms.PasswordInput(attrs={'type':'password','class':'forms__form forms__form--more_padding'})
        }
class SignupForm(forms.ModelForm):             
    class Meta:
        model = Signup
        fields = ['phone_number','password1','password2','email']
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        # Check if passwords match
        if password1 != password2:
            raise forms.ValidationError("رمز عبور و تکرار آن باید یکسان باشند.")

        return cleaned_data

    
