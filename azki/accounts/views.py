from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer,UserLoginSerializer
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
class UserRegister(APIView):
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.data)
        if ser_data.is_valid():
            user = ser_data.save()
            return Response({
                "message": "ثبت‌نام با موفقیت انجام شد",
                "user": UserLoginSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = [AllowAny,]

    def post(self, request):
        srz_data = UserLoginSerializer(data=request.data)
        if srz_data.is_valid():
            user = srz_data.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'ورود موفقیت آمیز بود',
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            },   status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)





class UserProfileViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = UserProfile.objects.all()

    def list(self, request):
        if not request.user.is_staff:
            return Response({"detail": "شما اجازه دیدن این لیست را ندارید."}, status=403)
        
        srz_data = ProfileSerializer(instance=self.queryset, many=True)
        return Response(data=srz_data.data)


    def retrieve(self, request, pk=None):
        profile = get_object_or_404(UserProfile, pk=pk)
        self.check_object_permissions(request, profile)
        srz_data = ProfileSerializer(profile)
        return Response(srz_data.data)


    def update(self, request, pk=None):
        profile = get_object_or_404(UserProfile, pk=pk)
        self.check_object_permissions(request, profile)  
        srz_data = ProfileUpdateSerializer(profile, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data)
        return Response(srz_data.errors, status=400)







    
   
    