# Todo List com Django

Uma aplicação simples de lista de tarefas (to-do list) desenvolvida com Django. O projeto permite organizar tarefas, definir prazo e prioridade, acompanhar a conclusão e editar ou excluir itens cadastrados.

## Funcionalidades

- Criar tarefas com título, descrição, prazo e prioridade;
- Visualizar todas as tarefas cadastradas;
- Marcar e desmarcar tarefas como concluídas;
- Editar tarefas existentes;
- Excluir tarefas;
- Exibir o prazo formatado e a prioridade de cada tarefa.

## Tecnologias utilizadas

- Python
- Django
- SQLite
- HTML, CSS e JavaScript

## Como executar localmente

1. Clone este repositório e entre na pasta do projeto:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd djangoTeste
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   No Windows, use:

   ```bash
   .venv\Scripts\activate
   ```

3. Instale o Django:

   ```bash
   pip install Django
   ```

4. Aplique as migrações:

   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```

6. Acesse `http://127.0.0.1:8000/todo/` no navegador.

## Estrutura principal

```text
todo/                 # App com modelo, views, URLs e templates das tarefas
templates/            # Template base e arquivos estáticos
djangoteste/          # Configurações do projeto Django
manage.py             # Comandos administrativos do Django
```