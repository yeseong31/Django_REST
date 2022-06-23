from django.shortcuts import get_object_or_404
from rest_framework import status, mixins, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import Book
from book.serializers import BookSerializer


# FBV -----------------------------------------------------------------------------------------
@api_view(['GET'])
def helloAPI(request):
    return Response('hello world!')


@api_view(['GET', 'POST'])
def booksAPI(request):
    """
    전체 도서 정보 조회 및 도서 정보 등록
    """
    if request.method == 'GET':
        books = Book.objects.all()
        # Serializer에서 여러 데이터에 대한 처리가 가능하도록 many=True 옵션 적용
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        # Serializer가 유효한 경우
        if serializer.is_valid():
            # 역직렬화를 통해 save() 후 create() 함수 동작
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def bookAPI(request, bid):
    """
    도서 한 권 정보 조회
    """
    book = get_object_or_404(Book, bid=bid)
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)


# CBV -----------------------------------------------------------------------------------------
class BooksAPI(APIView):
    def get(self, request):
        """
        전체 도서 정보 조회
        """
        books = Book.objects.all()
        # 여러 데이터에 대한 처리가 가능하도록 many=True 옵션 적용
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        도서 정보 등록
        """
        serializer = BookSerializer(data=request.data)
        # Serializer가 유효한 경우
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookAPI(APIView):
    """
    도서 한 권 정보 조회
    """
    def get(self, request, bid):
        book = get_object_or_404(Book, bid=bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)


# DRF mixins ----------------------------------------------------------------------------------
class BooksAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()  # 일반적으로 '모든' 데이터를 불러옴
    serializer_class = BookSerializer  # 해당 API에서 사용할 Serializer 등록

    def get(self, request, *args, **kwargs):
        """
        전체 목록 조회: mixins.ListModelMixin
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        도서 한 권 등록: mixins.CreateModelMixin
        """
        return self.create(request, *args, **kwargs)


class BookAPIMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()  # 일반적으로 '모든' 데이터를 불러옴
    serializer_class = BookSerializer  # 해당 API에서 사용할 Serializer 등록
    lookup_field = 'bid'  # Django 기본 모델의 pk가 아닌 bid를 pk로 사용하고 있다는 것을 알려 줘야 함

    def get(self, request, *args, **kwargs):
        """
        도서 한 권 조회: mixins.RetrieveModelMixin
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        도서 한 권 수정: mixins.UpdateModelMixin
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        도서 한 권 삭제: mixins.DestroyModelMixin
        """
        return self.destroy(request, *args, **kwargs)


# DRF generics --------------------------------------------------------------------------------
class BooksAPIGenerics(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookAPIGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'


# DRF Viewset & Router ------------------------------------------------------------------------
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
