from django.db import models
from datetime import date

# Create your models here.
class Todo(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=100, null=False, blank=False)
    description = models.TextField(verbose_name="Descrição", max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Data de entrega", null=False, blank=False)
    finished_at = models.DateField(null=True, blank=True)
    class Meta:
        ordering = ["deadline"]

    def clean(self):
        from django.core.exceptions import ValidationError

        # não salva uma tarefa com data de entrega anterior à data atual
        if self.deadline and self.deadline < date.today():
            raise ValidationError({"deadline": "A data de entrega não pode ser anterior à data atual."})

        super().clean()

    def mark_has_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()