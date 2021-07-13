from rest_framework.views import APIView
from users.models import CustomUser, CustomAuth
from users.serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.auth import authenticate
from django.http import Http404




class UserApiView(APIView):

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk = pk)
        except CustomUser.DoesNotExist:
            return Http404


    def get(self, request, pk, format= None):
        users = self.get_object(pk)
        serializer = UserSerializer(users, many= True, context={"request": request})
        return Response(serializer.data)



class UserSignUp(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer





class LoginView(APIView):

    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email = email, password= password)
        if user:
            return Response({'token' : user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)




class LogoutView(APIView):

    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status= status.HTTP_200_OK)