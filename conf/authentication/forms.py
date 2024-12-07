from django import forms

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
