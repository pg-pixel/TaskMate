from django import forms 
from todolist_app.models import TodoList 

class TodoListForm(forms.ModelForm):
    
    class Meta:
        model = TodoList
        fields = ['Task', 'Done']
