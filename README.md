__Sistema de Empréstimos de EPI__

-> Projeto full-stack desenvolvido em Spring Boot (Backend) e HMTL+JS (Frontend) com persistência em banco de dados relacional. Este sistema permite o gerenciamento de empréstimos de equipamentos por usuários e colaboradores.

# Funcionalidades

- Cadastro de Usuários e Colaboradores
- Cadastro de Equipamentos
- Registro de Empréstimos de equipamentos
- Integração entre entidades com relacionamentos via chave estrangeira

# Tecnologias Necessárias e Utilizadas

*Backend*
- VSCode
- Java 17+
- Spring Boot
- MySQL
- Maven

*Frontend*
- HTML
- CSS
- JS

# Modelo Físico do Banco de Dados

O banco de dados possui as seguintes tabelas:
- Usuario
- Colaborador
- Equipamento
- Emprestimo

<____________________________PASSO A PASSO PARA RODAR A APLICAÇÃO____________________________>

1. CONFIGURAR O BANCO DE DADOS 

1. 1.1 Acesse seu MySQL e crie o banco:

CREATE DATABASE epi;

1. 1.2 Execute os comandos SQL fornecidos a seguir para criar as tabelas.
*Comandos SQL para criação das tabelas*

CREATE TABLE Colaborador (
    id_colaborador INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL
);

CREATE TABLE Usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL
);

CREATE TABLE Equipamento (
    id_equipamento INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    quantidade_equipamento INT NOT NULL CHECK (quantidade_equipamento >= 0)
);

CREATE TABLE Emprestimo (
    id_controle INT AUTO_INCREMENT PRIMARY KEY,
    id_colaborador INT NOT NULL,
    id_equipamento INT NOT NULL,
    data_entrega DATE NOT NULL,
    data_prevista_devolucao DATE NOT NULL,
    data_devolucao DATE NULL,
    status ENUM('Emprestado', 'Em uso', 'Fornecido', 'Devolvido', 'Danificado', 'Perdido') NOT NULL,
    observacao_devolucao TEXT NULL,
    
    CONSTRAINT fk_colaborador FOREIGN KEY (id_colaborador) 
        REFERENCES Colaborador (id_colaborador)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT fk_equipamento FOREIGN KEY (id_equipamento) 
        REFERENCES Equipamento (id_equipamento)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

________________________________________________________________________________________________________________________________________________________________________________________________________________________

2. <-------------------- CLONAR REPOSITÓRIO -------------------->

2. 2.1 Com seu VS Code aberto abra o terminal e digite o seguinte comando para clonar o repositório

git clone https://github.com/Artrite/EPIControl.git
cd EPIControl

3. <-------------------- CONFIGURANDO O "application.properties" -------------------->

3. 3.1 No caminho src/main/resources/application.properties, adicione ou edite com suas credenciais:

spring.application.name=EPI

spring.jpa.show-sql=true
spring.datasource.url=jdbc:mysql://localhost:3306/epi
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.datasource.username=root
spring.datasource.password=*SUA SENHA*

4. <-------------------- RODANDO O BACKEND -------------------->

4. 4.1 No caminho src/main/java/senai/EPI/EpiApplication.java, e clique no botão "Run" (Canto superior direito).

# OUTRA OPÇÃO
4. 4.2 No terminal, execute:

./mvnw spring-boot:run

*A aplicação backend estará disponível em:*
http://localhost:8080/

5. <-------------------- RODANDO O FRONTEND -------------------->

5. 5.1 No caminho EPIControl/FrontEnd/EPIFront/findAllUser.html, e clique no botão "Run" (Canto superior direito).
