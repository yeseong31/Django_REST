from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from todo.forms import TodoForm
from todo.models import Todo
from todo.serializers import TodoSimpleSerializer, TodoDetailSerializer, TodoCreateSerializer


def todo_list(request):
    """
    TO DO 전체 목록 조회
    """
    todos = Todo.objects.filter(complete=False)
    return render(request, 'todo/todo_list.html', {'todos': todos})


def todo_detail(request, pk):
    """
    TO DO 상세 조회
    """
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})


def todo_post(request):
    """
    TO DO 생성
    """
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_post.html', {'form': form})


def todo_edit(request, pk):
    """
    TO DO 수정
    """
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_post.html', {'form': form})


def done_list(request):
    """
    TO DO Done 목록
    """
    dones = Todo.objects.filter(complete=True)
    return render(request, 'todo/done_list.html', {'dones': dones})


def todo_done(request, pk):
    """
    TO DO 완료
    """
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    return redirect('todo_list')


# APIView -------------------------------------------------------------------------------------------------------------
class TodosAPIView(APIView):
    def get(self, request):
        """
        To Do 전체 조회
        """
        todos = Todo.objects.filter()
        serializer = TodoSimpleSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        To do 생성
        """
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoAPIView(APIView):
    def get(self, request, pk):
        """
        To do 상세 조회
        """
        todo = get_object_or_404(Todo, id=pk)  # rest_framework.generics의 get_object_or_404
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoCreateSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoneTodosAPIView(APIView):
    def get(self, request):
        """
        To Do 완료 목록 조회
        """
        dones = Todo.objects.filter(complete=True)
        serializer = TodoSimpleSerializer(dones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DoneTodoAPIView(APIView):
    def get(self, request, pk):
        """
        To Do 완료 처리
        """
        done = get_object_or_404(Todo, id=pk)
        done.complete = True
        done.save()
        serializer = TodoDetailSerializer(done)
        return Response(serializer.data, status=status.HTTP_200_OK)
