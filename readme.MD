### Curso Técnico de Desenvolvimento de Sistemas - Senai Itapeva
![Imagem de capa](/gifs/capabackend.gif)

**Descrição:**

Esta API RESTFUL, desenvolvida com Flask e integrada ao Firebase Firestore, oferece uma solução completa para gerenciar um banco de dados de charadas. Ela fornece endpoints específicos para diversas operações, incluindo inserção, busca (aleatória e por ID), atualização e exclusão de charadas. A integração com o Firebase Firestore garante escalabilidade e confiabilidade para o armazenamento de dados.

## Índice

* [Funcionalidades](#funcionalidades)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Endpoints](#endpoints)
* [Banco de Dados (Firestore)](#banco-de-dados-firestore)
* [Instalação](#instalação)
* [Execução](#execução)
* [Autor](#autor)
* [Licença](#licença)

## Funcionalidades

* Busca de charadas aleatórias.
* Busca de charadas por ID.
* Adição de novas charadas.
* Atualização de charadas existentes.
* Exclusão de charadas.

## Tecnologias Utilizadas

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![image](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)

## Endpoints

* **GET `/`**: Verifica se a API está funcionando. Retorna uma mensagem de confirmação.

* **GET `/charadas`**: Retorna uma charada aleatória do banco de dados.
    * **Resposta (200 OK):**  `{ "pergunta": "...", "resposta": "..." }`
    * **Resposta (404 Not Found):** `{"mensagem": "ERRO, nenhuma charada encontrada"}`

* **GET `/charadas/id/<id>`**: Retorna a charada com o ID especificado.
    * **Resposta (200 OK):** `{"id": <id>, "pergunta": "...", "resposta": "..."}`
    * **Resposta (404 Not Found):** `{"mensagem": "Charada não encontrada"}`

* **POST `/charadas`**: Adiciona uma nova charada ao banco de dados. Requer um corpo JSON com os campos `pergunta` e `resposta`.
    * **Request Body:** `{"pergunta": "...", "resposta": "..."}`
    * **Resposta (201 Created):** `{"Mensagem": "Charada cadastrada com sucesso"}`
    * **Resposta (400 Bad Request):** `{"mensagem": "Erro, campos pergunta e resposta são obrigatórios"}`

* **PUT `/charadas/<id>`**: Atualiza uma charada existente. Requer um corpo JSON com os campos `pergunta` e `resposta`.
    * **Request Body:** `{"pergunta": "...", "resposta": "..."}`
    * **Resposta (200 OK):** `{"mensagem": "Charada atualizada com sucesso!"}`
    * **Resposta (400 Bad Request):** `{"mensagem": "Erro. Campos pergunta e resposta são obrigatórios"}`
    * **Resposta (404 Not Found):** `{"mensagem": "Erro. Charada não encontrada!"}`

* **DELETE `/charadas/<id>`**: Exclui uma charada.
    * **Resposta (200 OK):** `{"mensagem": "Charada excluída com sucesso!"}`
    * **Resposta (404 Not Found):** `{"mensagem": "Erro. Charada não encontrada"}`


## Banco de Dados (Firestore)

A API utiliza o Firebase Firestore para armazenar as charadas.  As charadas são armazenadas em uma coleção chamada `charadas`, com campos para `id`, `pergunta` e `resposta`. Um documento separado em uma coleção `controle_id` gerencia o ID sequencial.

## Instalação

1.  Clone este repositório: `git clone <repositório>`
2.  Navegue até o diretório do projeto: `cd <diretório>`
3.  Instale as dependências: `pip install -r requirements.txt`
4.  Configure o Firebase: Coloque o arquivo `ServiceAccountKey.json` no mesmo diretório do `app.py`.

## Execução

Para executar a API, execute o comando: `python app.py`

A API será executada em modo de debug na porta 5000 (localhost:5000).

## Autor

- Richard - https://github.com/Richard15151 - richard.oliveira.senai@gmail.com

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.