from categories.models import Categories
from categories.serializer import CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated




class AllCategories(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format= None):
        categoreis = Categories.objects.all()
        serializer = CategorySerializer(categoreis, many= True, context={"request": request})
        return Response(serializer.data)