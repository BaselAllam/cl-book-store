from books.models import Books
from books.serializer import BooksSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AllBooks(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        books = Books.objects.all()
        serializer = BooksSerializer(books, many= True, context={"request": request})
        return Response(serializer.data)





class SearchByCategory(generics.ListAPIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = BooksSerializer

    def get_queryset(self):
        category = self.kwargs.get('category', None)
        return Books.objects.all().filter(category = category)





class SearchByBookName(generics.ListAPIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = BooksSerializer

    def get_queryset(self):
        book = self.kwargs.get('bookTitle', None)
        return Books.objects.all().filter(book_title = book)