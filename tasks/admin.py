from django.contrib import admin

from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "deadline",
        "created_at",
        "finished_at",
    )

    search_fields = (
        "title",
    )

    list_filter = (
        "deadline",
        "finished_at",
    )

    ordering = (
        "-created_at",
    )