from rest_framework import serializers
from .models import FireInsurance, MobileInsurance, InsuranceCompany, SoldInsurance


# سریالایزر بیمه آتش‌سوزی
class FireInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireInsurance
        fields = [
            'id', 
            'name', 
            'insurance_company', 
            'price', 
            'property_type', 
            'build_type', 
            'build_age', 
            'coverage_amount', 
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


# سریالایزر بیمه موبایل
class MobileInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileInsurance
        fields = [
            'id', 
            'name', 
            'brand', 
            'price', 
            'insurance_company', 
            'coverage_amount', 
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


# سریالایزر شرکت‌های بیمه
class InsuranceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceCompany
        fields = [
            'id', 
            'name', 
            'address', 
            'phone_number', 
            'email', 
            'established_date'
        ]
        read_only_fields = ['id']


# سریالایزر خرید بیمه
class SoldInsuranceSerializer(serializers.ModelSerializer):
    # جزئیات بیمه مرتبط با خرید
    insurance_detail = serializers.SerializerMethodField()

    class Meta:
        model = SoldInsurance
        fields = [
            'id', 
            'user', 
            'insurance_type', 
            'insurance_id', 
            'price', 
            'created_at', 
            'insurance_detail'
        ]
        read_only_fields = ['id', 'created_at', 'insurance_detail']

    def get_insurance_detail(self, obj):
        """
        بازگرداندن اطلاعات جزئی بیمه بر اساس نوع بیمه (آتش‌سوزی یا موبایل)
        """
        if obj.insurance_type == "fire":
            insurance = FireInsurance.objects.filter(id=obj.insurance_id).first()
            return FireInsuranceSerializer(insurance).data if insurance else None
        elif obj.insurance_type == "mobile":
            insurance = MobileInsurance.objects.filter(id=obj.insurance_id).first()
            return MobileInsuranceSerializer(insurance).data if insurance else None
        return None


# سریالایزر برای لیست خریدهای کاربر
class UserPurchasesSerializer(serializers.ModelSerializer):
    insurance_detail = serializers.SerializerMethodField()

    class Meta:
        model = SoldInsurance
        fields = [
            'id', 
            'insurance_type', 
            'insurance_id', 
            'price', 
            'created_at', 
            'insurance_detail'
        ]

    def get_insurance_detail(self, obj):
        """
        جزئیات بیمه مرتبط با خرید برای نمایش در لیست خریدها
        """
        if obj.insurance_type == "fire":
            insurance = FireInsurance.objects.filter(id=obj.insurance_id).first()
            return FireInsuranceSerializer(insurance).data if insurance else None
        elif obj.insurance_type == "mobile":
            insurance = MobileInsurance.objects.filter(id=obj.insurance_id).first()
            return MobileInsuranceSerializer(insurance).data if insurance else None
        return None