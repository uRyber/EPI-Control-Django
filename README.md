# Sistema de Gestão de EPIs

Este projeto é um sistema para a gestão de Equipamentos de Proteção Individual (EPIs), permitindo o cadastro de colaboradores e equipamentos, o registro de empréstimos e a visualização de relatórios.

### Funcionalidades

* **Dashboard/Home:** Uma página inicial para navegação.
* **Cadastros:**
    * **Colaboradores:** CRUD (Criar, Ler, Atualizar e Deletar) de colaboradores.
    * **Equipamentos:** CRUD (Criar, Ler, Atualizar e Deletar) de equipamentos, com controle de quantidade em estoque.
* **Ações:**
    * **Controle de EPI:** Registro de empréstimos de equipamentos a colaboradores.
* **Relatórios:**
    * **Empréstimos:** Listagem completa de todos os empréstimos.
* **Busca:** Campo de busca funcional em todas as listagens para facilitar a localização de dados.

### Requisitos para Rodar o Projeto

Para executar o projeto, você precisa ter as seguintes ferramentas instaladas:

* **Python 3.x:** O projeto foi desenvolvido com uma versão recente do Python.
* **pip:** O gerenciador de pacotes do Python.
* **Django** Framework

### Como Rodar o Projeto

Colocando o projeto em funcionamento:

1.  **Clone o repositório:**
    Abra o VSCODE e abra terminal e execute o comando:

    git clone https://github.com/uRyber/EPI-Control-Django.git

2.  **Acesse a pasta do projeto:**
  
    cd EPI-Control-Django

3.  **Crie e ative um ambiente virtual (recomendado):**
    Isolar as dependências do projeto.
    
    python -m venv projeto_epi

    # Ativa o ambiente virtual (no Windows)
    cd projeto_epi/Scripts/activate

    # Ativa o ambiente virtual (no macOS/Linux)
    source venv/bin/activate

    # Ao final de ativar o  ambiente virtual volte 2 pastas

    cd ..

    cd ..

4.  **Instale as dependências:**
    Com o ambiente virtual ativado, instale o Django.
 
    pip install django

5.  **Configure o banco de dados:**
    O projeto utiliza o banco de dados padrão do Django, o SQLite. Você precisa executar as migrações para criar as tabelas no banco de dados.

    python manage.py makemigrations
    python manage.py migrate


6.  **Execute o servidor de desenvolvimento:**
    Inicie o servidor local para acessar o projeto pelo navegador.

    python manage.py runserver


7.  **Acesse o sistema:**
    Abra o seu navegador e acesse o endereço:

    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


O sistema estará pronto para uso.
