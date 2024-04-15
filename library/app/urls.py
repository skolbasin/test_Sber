from django.urls import path

from .views import (LibraryList,
                    UserList,
                    BookList,
                    facility_libraries_view,
                    users_by_age_view,
                    books_by_publishing_house_view,

                    )

app_name = 'library'


urlpatterns = [
    path('ll/', LibraryList.as_view(), name='libraries'),
    path('ul/', UserList.as_view(), name='users'),
    path('bl/', BookList.as_view(), name='books'),
    path('fll/', facility_libraries_view, name='facility_libraries'),
    path('ulm/', users_by_age_view, name='selected_users'),
    path('sbl/', books_by_publishing_house_view, name='selected_books'),


]
