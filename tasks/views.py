from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from .models import Todo


class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "description", "deadline"]
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Tarefa criada com sucesso!")
        return response

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "description", "deadline"]
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Tarefa atualizada com sucesso!")
        return response

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)

        if todo.finished_at:
            messages.info(request, "Esta tarefa já está concluída.")
        else:
            todo.mark_has_complete()
            messages.success(request, "Tarefa concluída com sucesso!")

        return redirect("todo_list")