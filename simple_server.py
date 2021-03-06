"""
простой проект который создает на компьютере сервер
главное это создать папку и внутри нее положить скрипт и 
файл с index.html c текстом ниже
после этого просто вбиваем в браузере 
http://localhost:8080/ 
и сайт работает
"""

from http.server import HTTPServer,CGIHTTPRequestHandler
server_data = ("localhost", 8080)
server = HTTPServer(server_data, CGIHTTPRequestHandler)
server.serve_forever()

"""
<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">      
    <title>Document</title>
    <style>
        body {
            background: #333;
            color: rgb(60, 255, 34);
        }
    </style>
</head>
<body>
    <h1>Привет Питонщики!!!</h1>
    <p> Еще текст </p>
</body>
</html>
"""
