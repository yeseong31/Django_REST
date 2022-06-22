from django.urls import path

from book.views import helloAPI, booksAPI, bookAPI, BooksAPIMixins, BookAPIMixins

urlpatterns = [
    path('hello/', helloAPI),
    path('', booksAPI),
    path('<int:bid>/', bookAPI),

    # ----- DRF mixins -----
    path('mixins/', BooksAPIMixins.as_view()),
    path('mixins/<int:bid>/', BookAPIMixins.as_view())
]
