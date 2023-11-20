[en-us]

# Final Project - Control and Automation UFMG

Welcome to the Final Project developed by Wallasce Leite as part of the Control and Automation Engineering course at UFMG. The goal of this project is to supervise a thermoelectrically controlled box using the OPC communication protocol. To achieve this, a Web Supervisory System has been created using Django, which includes an OPC Client that communicates with the OPC Server running on the plant to be supervised.

## Installation

To use this project, some prerequisites need to be installed:

    Python 3.7 or higher
    Serial library
    opcua-asyncio library

## Project Execution
### Thermoelectric OPC Server:
Navigate to the server folder:

    cd server

Execute the server:

    python Server.py

### WebSite with OPC Client:
Activate the Virtual Environment:

    venv\Scripts\activate.bat

Navigate to the supervisorySite folder:

    cd supervisorySite

Start the server:

    python manage.py runserver

### Test OPC Server:
Navigate to the server folder:

    cd server

Execute the desired server:

    python <ServerFileName>

(The ServerFileName can be serverTestReadOnly.py or serverTestWithWrite.py)

____
[pt-br]
# Projeto Final de Curso - Controle e Automação UFMG

Bem-vindo ao Projeto Final de Curso desenvolvido por Wallasce Leite como parte do curso de Engenharia de Controle e Automação na UFMG. O objetivo deste projeto é realizar a supervisão de uma caixa termoelétrica controlada, utilizando o protocolo de comunicação OPC. Para isso, foi criado um Supervisório Web desenvolvido em Django, contendo um Cliente OPC que se comunica com o Servidor OPC em execução na planta a ser supervisionada.

## Instalação

Para utilizar este projeto, é necessário realizar algumas instalações prévias:

    Python 3.7 ou superior
    Biblioteca Serial
    Biblioteca opcua-asyncio

## Execução do Projeto

### Servidor OPC da Caixa Termoelétrica:

Navegue até a pasta do servidor:

    cd server

Execute o servidor:

    python Server.py

### WebSite com Cliente OPC:

Ative o Ambiente Virtual:

    venv\Scripts\activate.bat

Navegue até a pasta supervisorySite:

    cd supervisorySite

Inicie o servidor:

    python manage.py runserver

### Servidor OPC de Teste:

Navegue até a pasta do servidor:

    cd server

Execute o servidor desejado:

    python <ServerFileName>

(O ServerFileName pode ser serverTestReadOnly.py ou serverTestWithWrite.py)

