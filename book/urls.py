from django.urls import path

from book.views import helloAPI, booksAPI, bookAPI, BooksAPIMixins, BookAPIMixins, BooksAPI, BookAPI, BooksAPIGenerics, \
    BookAPIGenerics

urlpatterns = [
    # ----- FBV -----
    path('hello/', helloAPI),
    path('fbv/', booksAPI),
    path('fbv/<int:bid>/', bookAPI),

    # ----- CBV -----
    path('cbv/', BooksAPI.as_view()),
    path('cbv/<int:bid>/', BookAPI.as_view()),

    # ----- DRF mixins -----
    path('mixins/', BooksAPIMixins.as_view()),
    path('mixins/<int:bid>/', BookAPIMixins.as_view()),

    # ----- DRF generics -----
    path('generics/', BooksAPIGenerics.as_view()),
    path('generics/<int:bid>/', BookAPIGenerics.as_view())
]
