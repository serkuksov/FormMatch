from pprint import pprint

import requests
from pymongo import MongoClient

from config import settings

# Пример тестовых данных
TEST_DATA = [
    {"name": "Form template 1", "field1": "string", "field2": "email"},
    {"name": "Form template 2", "field3": "phone", "field4": "date"},
    {"name": "Form template 3", "field1": "string", "field4": "date"},
]

REQUEST_DATA = [
    {"field1": "value1", "field2": "value2"},
    {"field1": "value1", "field2": "ser.kuksov@mail.ru"},
    {"field3": "89270306000"},
    {"field3": "+79270306000", "field4": "12.12.2023"},
    {"field3": "+7927030600770", "field4": "2023-12-12"},
    {"field4": "2023-12-12"},
]

# def start_docker_container():
#     try:
#         subprocess.run(["docker-compose", "up", "--build", "-d"], check=True)
#     except subprocess.CalledProcessError as e:
#         print(f"Ошибка: {e}")
#
#
# def stop_docker_container():
#     try:
#         subprocess.run(["docker-compose", "down"])
#     except subprocess.CalledProcessError as e:
#         print(f"Ошибка: {e}")


def init_db():
    """Наполнение MongoDB тестовыми данными"""
    # settings.MONGODB_HOST = "localhost"
    client = MongoClient(settings.MONGODB_URL)
    db = client[settings.MONGODB_DB]
    collection = db.get_collection("form_match")
    if collection.count_documents({}) == 0:
        collection.insert_many(TEST_DATA)
        print("Выполнена загрузка данных в базу данных следующего вида:")
        pprint(TEST_DATA)
    else:
        print("БД уже наполнена")


def test_request():
    url = "http://web-app:8000/get_form"
    for params in REQUEST_DATA:
        response = requests.post(url, params=params)
        print(f"Выполнен POST запрос на адрес: {response.url}")
        print(f"Получен ответ: {response.json()}")
        print("-"*20)


if __name__ == '__main__':
    init_db()
    test_request()
