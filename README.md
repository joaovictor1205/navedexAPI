# Introdução

Para a resolução do desafio, utilizei as seguintes tecnologias:

- Python, como linguagem de programação;

- Django Framework, como framework de desenvolvimento web para o backend;

- Django Rest Framework, como biblioteca para o Django Framework para criação de APIs Restful;

- Django Environ, como biblioteca para manipular variáveis de ambiente sensíveis à aplicação;

- Django Rest Framework JWT, como biblioteca para o Django Framework para criação de tokens para autenticar um usuário ao fazer o login;

- Pillow, como biblioteca para o Django Framework para manipulação de imagens da aplicação que utilizei para cadastrar um avatar para um Naver;

- PostgreSQL, como SGBD para armazenar, acessar, atualizar e deletar informações no banco de dados;

- Requests, como biblioteca para o Django Framework para testes automatizados de requisições HTTP.

- Insomnia, para realizar as requisições HTTP

# Configurações

### Ambiente Virtual

Ao ter acesso aos arquivos, primeiro deve-se criar o ambiente de desenvolvimento (vitualenv) e instalar todas as dependências, utilizando:

```bash
python3 -m venv env
pip install -r requirements.txt
```

### Variáveis de ambiente

Depois de ter todas as dependências instaladas, deve-se acrescentar algumas variáveis de ambiente:

- Primeiro deve-se criar um arquivo '.env' na pasta navedexAPI, ou seja, na mesma pasta do arquivo settings.py
- No arquivo '.env' colocar as seguintes variáveis:

```bash
SECRET_KEY=y)afr90fx@cv)@@lb@n!2)dhq+p3j+cdf!lv^5(!)2_n4swmj7
DB_NAME='nome do banco criado'
DB_USER='nome do usuário do banco'
DB_PASSWORD='senha do banco'
DB_HOST='endereço do banco'
DB_PORT='porta que o banco está rodando'
```

### Migrations

- Agora deve-se rodar as migrações para o banco ser preenchido com as tabelas necessárias à aplicação:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Django Admin

- Após estas configurações iniciais, o projeto já estará pronto para uso, logo, deve-se criar um super user para o acesso do Django Admin (caso seja necessário):

```bash
python manage.py createsuperuser
```


# Pensando no problema

Antes de iniciar qualquer aplicação, eu gosto de resolver o problema primeiro na minha cabeça e 'modelar' o banco fazendo alguns rascunhos e só então iniciar a codificação. Para a resolução do NavedexAPI eu modelei da seguinte forma:

- Herdei o model User do Django Framework para a criação de novos usuários;
- Criei um model de Naver, que possui uma chave estrangeira para o model de User, sendo assim, um User pode 'ser responsável' por vários Navers, e um Naver sempre vai ter um User vinculado;
- Criei um model de Projeto, que possui uma chave estrangeira para o model de Naver, sendo assim, um Naver possui um ou mais projetos vinculados, ou até mesmo nenhum;
- Para a criação de nova conta (signup), deve-se informar os campos 'username', 'password' e 'email', os campos 'username' e 'email' possuem suas validações necessárias;
- Com a conta criada, deve-se informar os campos 'username' e 'password' para a rota de autenticação (login) para receber um JWT para conseguir ter acesso às outras rotas da API.

# Rotas

### Autenticação
- Registration/Signup
```bash
url: localhost:8000/api/register/
body: "username", "password", "email"
```

- Login/Authentication
```bash
url: localhost:8000/token/
body: "username", "password"
retorno: JWT
```


> As próximas rotas só poderão ser acessadas passando o token na variável Authorization do header da requisição: 'JWT + token recebido no login'

> O usuário que está fazendo a requisição HTTP somente tem permissão de visualizar as informações de Navers vinculados à ele 


### Rotas para Navers
- Naver List (GET)
```bash
url: http://127.0.0.1:8000/api/navers/

Obs: Aqui pode-se utilizar filtros nos parâmetros da url passando "name"ou "admission_date"
ou "job_role"
```

- Naver List por id (GET)
```bash
url: http://127.0.0.1:8000/api/navers/"id"
```

- Naver Store (POST)
```bash
url: http://127.0.0.1:8000/api/navers/
body: Obrigatórios "id do user" e "name" para o Naver
```

- Naver Update (PUT)
```bash
url: http://127.0.0.1:8000/api/navers/"id"
body: Obrigatórios "id do user" e "name" para o Naver

obs: A requisição de PUT só é permitida para o User responsável pelo Naver
```
- Naver Delete (DELETE)
```bash
url: http://127.0.0.1:8000/api/navers/"id"

obs: A requisição de DELETE só é permitida para o User responsável pelo Naver
```

### Rotas para Projetos

> O usuário que está fazendo a requisição HTTP somente tem permissão de visualizar as informações de Navers vinculados à ele 


- Projeto List (GET)
```bash
url: http://127.0.0.1:8000/api/navers/

Obs: Aqui pode-se utilizar filtros nos parâmetros da url passando "name"
```

- Projeto List por id (GET)
```bash
url: http://127.0.0.1:8000/api/navers/"id"
```

- Projeto Store (POST)
```bash
url: http://127.0.0.1:8000/api/navers/
body: Obrigatórios "id do naver" e "name" para o Naver
```

- Projeto Update (PUT)
```bash
url: http://127.0.0.1:8000/api/navers/"id"
body: Obrigatórios "id do naver" e "name" para o Naver

obs: A requisição de PUT só é permitida para o User responsável pelo Naver
```
- Projeto Delete (DELETE)
```bash
url: http://127.0.0.1:8000/api/navers/"id"

obs: A requisição de DELETE só é permitida para o User responsável pelo Naver
```

# Testes

- Na raíz do projeto tem-se o arquivo 'automated_tests.py', onde se encontram todos os testes utilizados para verificar a funcionalidade das rotas;


# Considerações Finais

- Por questões de melhor visualização coloquei um paginator de tamanho 2, que pode ser alterado na variável 'PAGE_SIZE' no arquivo settings.py;
- Os uploads de fotos para o avatar de um Naver vão para a pasta 'uploads' na raiz do projeto, ou seja, no mesmo nível do arquivo manage.py.


## Referências
[DRF + Vue (Udemy)](https://www.udemy.com/course/the-complete-guide-to-django-rest-framework-and-vue-js)

[DRF + JWT (Youtube)](https://www.youtube.com/watch?v=jEXQqNtjNJc)

[DRF + Signup (Youtube)](https://www.youtube.com/watch?v=2pzqjmNAsxM&list=PLx-q4INfd95GjSD6I6SsmXhm32ZuxWXpk&index=2)

[DRF (Doc)](https://www.django-rest-framework.org/)

