# Intro Python Django

Projeto feito para **estudos do framework Django**. A aplicação permite gerenciar tarefas (modelo `Todo`) com páginas para listar, criar, editar, excluir e concluir.

## O que tem neste projeto

- **CRUD** de tarefas usando `ListView`, `CreateView`, `UpdateView` e `DeleteView`.
- Modelo `Todo` com validação (ex.: `deadline` não pode ser no passado) e campo `description` opcional.
- Interface com **templates HTML** usando Bootstrap.
- Uso de **Django Messages** para feedback nas ações do usuário.
- Testes automatizados (`python manage.py test`).

## Estrutura (visão geral)

- `setup/` : projeto Django (settings, urls, asgi/wsgi)
- `tasks/` : app com model, views e templates
- `tasks/templates/` : telas da aplicação

## Como rodar localmente

1. Crie e ative um ambiente virtual:
   - `python -m venv .venv`
   - Ative o ambiente virtual (Windows): `.venv\Scripts\activate`

2. Instale dependências:
   - `pip install -r requirements.txt`

3. Rode migrações:
   - `python manage.py makemigrations`
   - `python manage.py migrate`

4. Inicie o servidor:
   - `python manage.py runserver`

## Comandos úteis

- Rodar testes:
  - `python manage.py test`
- Verificar problemas no projeto:
  - `python manage.py check`
- Criar migrações após alterar modelos:
  - `python manage.py makemigrations`

## Observações

Este repositório é voltado para prática e consolidação de conceitos do Django:
views genéricas, modelagem com ORM, templates, migrações e testes.

