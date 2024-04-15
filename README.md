# Тестовое задание на Django

Условие: Создать три модели: Библиотека, Пользователь, Книга. Требуется придумать по два запроса с использованием: select_related, prefetch, prefetch_related. Все запросы обернуть в API.

## Как запустить проект:
1. Клонировать репозиторий:
```
git clone https://github.com/skolbasin/test_Sber.git
```
2. Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
3. Выполнить миграции для создания структуры базы данных:
```
python manage.py makemigrations
python manage.py migrate
```
либо на Linux:
```
make migrate
```

4. Запустить сервер :
```
python manage.py runserver
```
либо на Linux:
```
make run
```
5. Создайте суперюзера
```
python manage.py createsuperuser
```
либо на Linux:
```
make superuser
```
6. После запуска сервера перейдите по адресу http://localhost:8000/admin и введи логин и пароль от суперюзера

## О проекте:
Задание было выполнено через Django и DRF(для создания API)

Сами модели расположены в приложении app в файле models.py и добавлены в админу с переводом на русский язык
![image](https://github.com/skolbasin/test_Sber/assets/111511890/d7829e1f-acd7-4928-8c7f-8e7c8c5b2794)

### Модель "Библиотека"
![image](https://github.com/skolbasin/test_Sber/assets/111511890/e9218cfd-d78d-4cb1-9e3f-ac279c6a69d4)

### Модель "Пользователь"

![image](https://github.com/skolbasin/test_Sber/assets/111511890/85b123d1-338e-4f69-abf9-9a7ee66b6613)

Примечание: составлена валидация для поля "Фамилия Имя"(находится в config.py), для создания пользователя загружать фото не обязательно

### Модель "Книга" 

![image](https://github.com/skolbasin/test_Sber/assets/111511890/a898ec7a-6569-450d-a524-7a58bfada53c)

API доступны по адресу: http://localhost:8000/api


DRF дает возможность при внесении модели в API, совершать с ней все необходимые запросы(GET, POST, HEAD, OPTIONS)
![image](https://github.com/skolbasin/test_Sber/assets/111511890/2fce2a61-ac1a-4d46-8397-766ec1a28956)
![image](https://github.com/skolbasin/test_Sber/assets/111511890/b8995eac-65fc-49a2-8571-aebfefd36120)
![image](https://github.com/skolbasin/test_Sber/assets/111511890/5b726e15-7743-4b62-a46c-de76feff8521)




