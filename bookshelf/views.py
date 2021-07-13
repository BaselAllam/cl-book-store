from bookshelf.models import BookShelf
from bookshelf.serializer import BookShelfSerailizer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated



class AllBookShelf(generics.ListAPIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = BookShelfSerailizer

    def get_queryset(self):
        user = self.kwargs.get('username', None)
        return BookShelf.objects.all().filter(user_id= user)




    def post(self, request, format= None):
        serializer = BookShelfSerailizer(request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)