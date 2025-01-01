from django.db import models

class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255,default=0)
    otp_code = models.CharField(max_length=6, blank=True, null=True) 
    entered_otp = models.CharField(max_length=6, blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
 
    def generate_otp(self):
        import random
        self.otp = str(random.randint(100000, 999999))
        self.save()

    def __str__(self):
        return self.phone_number

class Signup(models.Model):
    phone_number= models.CharField(max_length=11)
    email= models.EmailField()
    password1 = models.CharField(max_length=15)
    password2 = models.CharField(max_length=15) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    





