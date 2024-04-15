from rest_framework import serializers
from .models import Library, UserAccount, Book


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
