# Final_project
Задание 1 и 2.
Написаны два SQL запроса, с которыми можно ознакомиться в файле SQL.txt Первый запрос выводит список логинов курьеров с количеством их заказов в статусе «В доставке». Второй выводит все трекеры заказов и их статусы.

Автоматизация теста к API.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск теста выполняется командой pytesе
- Для запуска автотеста необходимо запустить сервис и подставить сгенерированную URL в файл configuration.py (URL_SERVICE =)

Автотест выполняет запрос на создание заказа, сохраняет номер трека заказа, выполняет запрос на получения заказа по треку заказа. Также есть проверка кода ответа = 200.
Прилагается скриншот запроса с ответом = 200 в файле Screenshot.png
