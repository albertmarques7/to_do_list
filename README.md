Lista de Tarefas - Seu Organizadador Pessoal

Este repositório contém um site simples de lista de tarefas, desenvolvido com Django REST Framework para a API e SQLite como banco de dados. Ele oferece um front-end básico para interagir com sua lista de tarefas.

Instalação e Execução

Clone o repositório:

git clone <https://github.com/albertmarques7/todolist_django.git>

Navegue para o diretório do projeto:

cd <nome do repositório>

Crie o ambiente virtual (recomendado):

python3 -m venv .venv
source .venv/bin/activate

Instale as dependências:

pip install -r requirements.txt

Crie o banco de dados:

python manage.py makemigrations
python manage.py migrate

Execute o servidor Django:

python manage.py runserver


O site estará acessível em http://127.0.0.1:8000/.

Como Usar

O front-end básico permite que você:

Adicione novas tarefas: Digite o nome da tarefa e pressione "Enter" para adicionar.

Visualize tarefas: Veja a lista de tarefas adicionadas.


Exclua tarefas: Clique no botão deletar ao lado da tarefa para removê-la.

Estrutura do Projeto

todo_app/: Contém o código principal da aplicação Django, incluindo modelos, visualizações, serializadores e URLs.

frontend/: Contém o código do front-end, usando HTML, CSS e JavaScript.

Personalização

Banco de dados: Para usar outro banco de dados, como PostgreSQL, modifique as configurações em todo_app/settings.py.

Front-end: O front-end é básico e pode ser personalizado com HTML, CSS e JavaScript.

API: Você pode adicionar novas funcionalidades à API usando o Django REST Framework.

Observações:

Este projeto é um exemplo simples e pode servir como ponto de partida para projetos mais complexos.

O front-end é básico e pode ser aprimorado com bibliotecas JavaScript como React ou Vue.js.

Para produção, é recomendável usar um servidor web como Apache ou Nginx.
