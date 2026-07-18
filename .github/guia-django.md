# Guia rápido do Django (para estudos)

## 1) Conceitos essenciais

- **Projeto** (ex.: `setup/`) concentra configurações e roteamento.
- **App** (ex.: `tasks/`) concentra uma funcionalidade do sistema.
- **Model** (`models.py`) define estrutura e regras no banco (ORM).
- **View** manipula requisições e retorna resposta (HTML/redirect/json).
- **Template** (`templates/`) renderiza HTML com dados do backend.

## 2) Fluxo típico de uma funcionalidade 

1. Model/fields em `models.py`.
2. Migrações: `makemigrations` + `migrate`.
3. Views (ex.: `ListView`, `CreateView`).
4. URLs em `setup/urls.py` apontando para as views.
5. Templates em `tasks/templates/`.
6. (Opcional) Validações em `clean()`/form.
7. Testes em `tasks/tests.py`.

## 3) Migrações e evolução do schema

- Sempre que alterar `models.py`, rode:
  - `python manage.py makemigrations`
  - `python manage.py migrate`

## 4) Mensagens do Django (feedback ao usuário)

 Use `django.contrib.messages` para retornar status de ações (ex.: sucesso ao criar/concluir).

