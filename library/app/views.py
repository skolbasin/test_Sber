from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Library, UserAccount, Book
from .serializers import LibrarySerializer, UserSerializer, BookSerializer


class LibraryList(ListCreateAPIView):
    """
    Список всех библиотек
    """
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


@api_view(['GET'])
def facility_libraries_view(request: Request) -> Response:
    """
    Список всех государственных библиотек
    """
    libraries = Library.objects.filter(state_facility=True)
    serializer = LibrarySerializer(libraries, many=True)
    return Response(serializer.data)


class UserList(ListCreateAPIView):
    """
    Список всех пользователей
    """
    queryset = UserAccount.objects.all().prefetch_related('books_taken')
    serializer_class = UserSerializer


@api_view(['GET'])
def users_by_age_view(request: Request) -> Response:
    """
    Список всех пользователей, старше заданного возраста
    """
    age = request.query_params.get('age', None)

    if age is not None:
        users = UserAccount.objects.filter(age__gt=int(age)).prefetch_related('books_taken')
    else:
        raise ValueError('Некорректно выполнен запрос, не указан возраст в URL')

    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


class BookList(ListCreateAPIView):
    """
    Список всех книг
    """
    queryset = Book.objects.all().select_related('library').prefetch_related('users')
    serializer_class = BookSerializer


@api_view(['POST'])
def books_by_publishing_house_view(request: Request) -> Response:
    """
    Список книг по названию издания
    """
    publishing_house = request.data.get('publishing', None)
    if publishing_house is not None:
        books = Book.objects.filter(publishing_house=publishing_house).select_related('library').prefetch_related('users')
    else:
        raise ValueError('Некорректно выполнен запрос, не указано название издания в запросе')

    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
