from django.db import models
from iranian_cities.fields import OstanField, ShahrestanField
from accounts.models import UserProfile





class InsuranceCompany(models.Model):
    name = models.CharField(max_length=100)  # نام شرکت بیمه
    established_date = models.DateField(null=True, blank=True)  # تاریخ تأسیس شرکت بیمه
    address = models.TextField(null=True, blank=True)  # آدرس شرکت
    phone_number = models.CharField(max_length=15, null=True, blank=True)  # شماره تلفن شرکت

    def __str__(self):
        return self.name

 



    

   


class FireInsurance(models.Model):
    INSURANCE_TYPES = [
        ('f', 'فلزی'),
        ('a', 'اجری'),
        ('b', 'بتنی'),
    ]
    property_TYPES = [
         ('a', 'یک واحد اپارتمان'),
        ('v', 'یک ساختمان ویلایی'),
        ('m', 'اپارتمان یا مجتمع'),

    ]
    Matters_TYPES = [
        ('c', 'کامل (بنا و لوازم خانه)'),
        ('l', 'لوازم خانه'),
        ('b', 'بنا'),
    ]

    # ارتباط با شرکت بیمه
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE, related_name='fire_insurances', default='no body')
    ostan = OstanField()  
    shahr = ShahrestanField() 
    Property_Type = models.CharField(max_length=10,choices=property_TYPES,default=' ',null=True, blank=True)
    Number_Of_Units = models.IntegerField(default='1')
    build_Type = models.CharField( max_length=10,choices=INSURANCE_TYPES,default=' ',null=True, blank=True)
    build_Age = models.PositiveIntegerField(null=True, blank=True)
    Insurance_Matters = models.CharField(max_length=20,choices=Matters_TYPES,default=' ',null=True, blank=True)
    build_Price = models.IntegerField(null=True, blank=True)
    thing_Price = models.IntegerField( null=True, blank=True)
    name_family = models.CharField(max_length=20,null=True, blank=True)
    national_code_Insurer = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.PositiveIntegerField  ( null=True, blank=True)
    birth_date = models.DateField( null=True, blank=True)
    Number_of_floors = models.PositiveIntegerField(null=True, blank=True, default='1')
    Exact_address = models.CharField(max_length=20,null=True,blank=True)
    floor = models.PositiveIntegerField(null=True, blank=True)
    unit = models.PositiveIntegerField(null=True, blank=True)
    tag = models.PositiveIntegerField(null=True, blank=True)
    Landline_number = models.PositiveIntegerField(null=True, blank=True)
    zip_code = models.PositiveIntegerField(null=True, blank=True)
    Expiration_date_previous_insurance = models.DateField(null=True,blank=True)
    def __str__(self):
        return self.user    







class MobileInsurance(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=20, null=True, blank=True)
    national_code = models.IntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    City = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.PositiveIntegerField(null=True, blank=True)

    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE, related_name='mobile_insurances', null=True, blank=True)
    # سایر فیلدها...
    def __str__(self):
        return f"Mobile Insurance - {self.name} ({self.phone_number})"









class SoldInsurance(models.Model):
    INSURANCE_TYPES = [
        ('fire', 'بیمه آتش‌سوزی'),
        ('mobile', 'بیمه موبایل'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sold_insurances')  # کاربر خریدار
    insurance_type = models.CharField(max_length=10, choices=INSURANCE_TYPES)  # نوع بیمه
    insurance_id = models.PositiveIntegerField()  # ID بیمه خریداری شده (FireInsurance یا MobileInsurance)
    purchase_date = models.DateTimeField(auto_now_add=True)  # تاریخ خرید
    price = models.BigIntegerField()  # مبلغ خرید

    def __str__(self):
        return f"{self.user} - {self.insurance_type} - {self.purchase_date}"