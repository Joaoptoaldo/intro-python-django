from datetime import timedelta
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from .models import Todo

class TodoTests(TestCase):
    def test_description_can_be_blank(self):
        todo = Todo(
            title="Teste",
            description="",
            deadline=timezone.localdate(),
        )
        # model deve permitir description vazia
        todo.full_clean()


    def test_deadline_cannot_be_in_the_past(self):
        yesterday = timezone.localdate() - timedelta(days=1)
        todo = Todo(
            title="Teste",
            description="qualquer",
            deadline=yesterday,
        )
        with self.assertRaises(ValidationError) as ctx:
            todo.full_clean()

        self.assertIn("deadline", ctx.exception.message_dict)

