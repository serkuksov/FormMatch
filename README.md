# FormMatch

FormMatch - это веб-приложение на основе FastAPI для определения шаблонов форм на основе переданных данных. Приложение использует MongoDB для хранения шаблонов форм и Pydantic для валидации данных.

## Особенности

- Поддерживается валидация данных 4-х типов:
1. Email
2. Номера телефонов России
3. Даты в формате `d.m.Y` и `Y-m-d`
4. Строки
- Хранение данных в MongoDB.
- Полностью асинхронная реализация.
- Приложение не предоставляет интерфейс для добавления тестовых данных шаблонов в БД

## Запуск с Docker + наполнение БД
* Скрипт наполняет БД данными `TEST_DATA` из файла `test_script.py` при первом запуске. 
* Очистка БД не предусмотрена. Потребуется стереть volumes.
* При каждом запуске происходт отправка тестовых запросов веб приложению с выводом информации в консоль контейнера `test-app`.
* Вы можете протестировать приложение в ручную например с использованием Postman.
1. Убедитесь, что Docker установлен на вашем компьютере.

2. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/serkuksov/FormMatch.git
   cd FormMatch

3. Запустите приложение с использованием Docker Compose:
   ```bash
   docker-compose up --build

4. Приложение будет доступно по адресу http://localhost:8000/get_form?param... где в качестве GET параметров *param* передаются названия полей и данные в них.
