from django.contrib import admin
from .models import MobileInsurance, FireInsurance , InsuranceCompany,Sale

admin.site.register(FireInsurance)
admin.site.register(MobileInsurance)
admin.site.register(InsuranceCompany)
admin.site.register(Sale)
