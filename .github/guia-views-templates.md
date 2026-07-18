# Boas práticas para views e templates

## Views genéricas

- `ListView`: renderiza lista de objetos.
- `CreateView`: cria objeto a partir de um formulário.
- `UpdateView`: edita objeto.
- `DeleteView`: confirma exclusão.

## Templates

- Mantenha `base.html` com estrutura geral (navbar, blocos e importações CSS).
- Use blocos como `{% block content %}` e `{% block page_title %}`.

