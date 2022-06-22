from django import forms

from todo.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        # 사용할 모델
        model = Todo
        # 모델의 속성
        fields = ['title', 'description', 'important']