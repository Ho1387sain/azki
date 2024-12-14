from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import FireInsurance, MobileInsurance, InsuranceCompany, SoldInsurance
from .serializers import (
    FireInsuranceSerializer,
    MobileInsuranceSerializer,
    InsuranceCompanySerializer,
    SoldInsuranceSerializer
)

# ویوی بیمه‌های آتش‌سوزی
class FireInsuranceListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        insurances = FireInsurance.objects.all()
        serializer = FireInsuranceSerializer(insurances, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FireInsuranceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FireInsuranceDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        insurance = get_object_or_404(FireInsurance, pk=pk)
        serializer = FireInsuranceSerializer(insurance)
        return Response(serializer.data)

    def put(self, request, pk):
        insurance = get_object_or_404(FireInsurance, pk=pk)
        serializer = FireInsuranceSerializer(insurance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        insurance = get_object_or_404(FireInsurance, pk=pk)
        insurance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ویوی بیمه‌های موبایل
class MobileInsuranceListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        insurances = MobileInsurance.objects.all()
        serializer = MobileInsuranceSerializer(insurances, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MobileInsuranceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MobileInsuranceDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        insurance = get_object_or_404(MobileInsurance, pk=pk)
        serializer = MobileInsuranceSerializer(insurance)
        return Response(serializer.data)

    def put(self, request, pk):
        insurance = get_object_or_404(MobileInsurance, pk=pk)
        serializer = MobileInsuranceSerializer(insurance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        insurance = get_object_or_404(MobileInsurance, pk=pk)
        insurance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ویوی خرید بیمه
class PurchaseInsuranceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user.profile
        insurance_type = request.data.get("insurance_type")
        insurance_id = request.data.get("insurance_id")
        price = request.data.get("price")

        if insurance_type not in ["fire", "mobile"]:
            return Response({"error": "نوع بیمه نامعتبر است."}, status=status.HTTP_400_BAD_REQUEST)

        insurance_model = FireInsurance if insurance_type == "fire" else MobileInsurance
        insurance = get_object_or_404(insurance_model, id=insurance_id)

        sold_insurance = SoldInsurance.objects.create(
            user=user,
            insurance_type=insurance_type,
            insurance_id=insurance.id,
            price=price,
        )
        return Response(
            {"message": "خرید با موفقیت انجام شد.", "sold_id": sold_insurance.id},
            status=status.HTTP_201_CREATED,
        )


# ویوی لیست خریدهای کاربر
class UserPurchasesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user.profile
        purchases = SoldInsurance.objects.filter(user=user)
        serializer = SoldInsuranceSerializer(purchases, many=True)
        return Response(serializer.data)