from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer, AuthorWithBooksSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def perform_create(self, serializer):
        name = serializer.validated_data['name']
        serializer.save(name = f"{name}!")

    def get_queryset(self):
        queryset = super().get_queryset()
        author_age = self.request.query_params.get('author_age')
        
        if author_age is not None:
            try:
                author_age = int(author_age)
            except ValueError:
                return queryset.none()
          
            queryset = queryset.filter(author__age__gte=author_age)
          
        return queryset


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        book_name = self.request.query_params.get('book_name')
        
        if book_name is not None:
            try:
                book_name = book_name
            except ValueError:
                return queryset.none()
          
            queryset = queryset.filter(book__name__contains=book_name)
          
        return queryset
    
    @action(detail=True, methods=["GET"])
    def get_author_with_id(self, request, pk):
        author = self.get_object()
        serializer = AuthorWithBooksSerializer(author) 
        return Response(serializer.data)
        