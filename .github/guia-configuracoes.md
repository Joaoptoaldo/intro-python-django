# Guia de configurações (setup/settings.py)

## Ajustes típicos

- **INSTALLED_APPS**
  - Apps do Django essenciais (admin, auth, sessions, staticfiles etc.).
  - `crispy_forms` e `crispy_bootstrap5` para formulários com Bootstrap.
  - `tasks.apps.TasksConfig` para registrar o app.

- **TEMPLATES**
  - `APP_DIRS = True` para buscar templates dentro de apps.

- **Database**
  - `DATABASES` configurado (ex.: sqlite local) via `DATABASE_URL` com fallback.

- **LANGUAGE/TIMEZONE**
  - `LANGUAGE_CODE = 'pt-br'`
  - `TIME_ZONE` alinhado ao contexto do usuário.

## Mensagens do Django

Quando necessário, pode-se configurar armazenamento de mensagens para evitar issues em redirects:
- `MESSAGE_STORAGE = "django.contrib.messages.storage.fallback.FallbackStorage"`

## Bootstrap / crispy-forms

- `CRISPY_TEMPLATE_PACK = "bootstrap5"`
- `crispy_forms` ajuda a renderizar `form` no template com a estilização adequada.

