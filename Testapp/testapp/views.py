from django.contrib.auth.models import User
from .serializers import RegisterSerializer,LoginSerializer
from rest_framework import generics
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import render
from rest_framework.views import APIView

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
  
  

def home(request):
    return render(request, 'index.html')


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        serializer = self.serializer_class(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            # Add your logic for handling successful registration here
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'errors': serializer.errors})


class LoginView(APIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer


    def post(self, request):
        serializer = self.serializer_class(data=request.POST)
        if serializer.is_valid():
            print(serializer.data)
            # Add your logic for handling successful registration here
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'errors': serializer.errors})