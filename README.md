# Intro Python Django

Projeto feito para **estudos do framework Django**. A aplicação permite gerenciar tarefas (modelo `Todo`) com páginas para listar, criar, editar, excluir e concluir.

## Conceitos praticados

- Estrutura de projetos Django
- MVT (Model-View-Template)
- Django ORM
- Generic Class-Based Views
- ModelForms
- Django Admin
- Messages Framework
- Validação de modelos
- Migrações
- Testes automatizados

## O que tem neste projeto

- **CRUD** de tarefas utilizando Generic Class-Based Views (`ListView`, `CreateView`, `UpdateView` e `DeleteView`).
- Modelo `Todo` com validação (ex.: `deadline` não pode ser no passado) e campo `description` opcional.
- Interface com **templates HTML** usando Bootstrap.
- Uso de **Django Messages** para feedback nas ações do usuário.
- Testes automatizados (`python manage.py test`).
- Formulários implementados com **ModelForm** para separação da lógica de apresentação.
- Rotas organizadas por aplicação através de `tasks/urls.py`.
- Painel administrativo configurado com **Django Admin** para gerenciamento das tarefas.

## Estrutura (visão geral)

- `setup/` : projeto Django (settings, urls, asgi/wsgi)
- `tasks/` : app com admin, models, forms, views e templates
- `tasks/templates/` : telas da aplicação

## Tecnologias utilizadas

- Python 3
- Django
- Bootstrap 5
- SQLite

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

5. (Opcional) Acesse o Admin do Django
   1. Crie um usuário admin:
      - `python manage.py createsuperuser`
   2. Acesse no navegador:
      - http://127.0.0.1:8000/admin/


## Comandos úteis

- Rodar testes:
  - `python manage.py test`
- Verificar problemas no projeto:
  - `python manage.py check`
- Criar migrações após alterar modelos:
  - `python manage.py makemigrations`

## Observações

Este repositório foi desenvolvido para praticar os principais conceitos do Django, incluindo Generic Class-Based Views, ModelForms, ORM, Templates, Django Admin, organização de rotas por aplicação, migrações, validações e testes automatizados.