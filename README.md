# Projeto-Final-de-Curso
Projeto Final de Curso do curso de Engenharia de Controle e Automacao da UFMG.
Desenvolvido por Wallasce Leite.

# Instalação

Para usar esse projeto é necessário algumas intalações:

Python3.7>
Serial
opcua-asyncio

# Executar o Projeto

## Sevidor OPC da Caixa Termoelétrica basta:
    
    1 - Entrar na pasta Server
        cd server
    2 - Executar o servidor
        python Server.py

## WebSite que contém o ClienteOPC basta:
    
    1 - Ativar o Ambiente Virtual:
        venv\Scripts\activate.bat

    2 - Entrar na supervisorySite:
        cd supervisorySite

    3 - Iniciar servidor:
        python manage.py runserver

## Servidor OPC de teste:
    
    1 - Entrar na pasta Server
        cd server
    
    2 - Executar o servidor desejado
        python <ServerFileName>
    
    O ServerFileName pode ser serverTestReadOnly.py ou serverTestWithWrite.py