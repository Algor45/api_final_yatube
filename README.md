# Api интерфейс для проекта yatube.
## Описание
Данный проект является интерфейсом API для проекта yatube.

Аутентификация в проекте построена на **JWT-токенах**.

Неаутентифицированные пользователи имеют разрешение только на чтение.

Аутентифицированные пользователи могут создавать контент , а также изменять только свой контент.


## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Algor45/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
py -3.7 -m venv env
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
py -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Перед использованием сгенерируйте новый секретный ключ
и замените им ключ по умолчанию в файле:

```
yatube_api/yatube_api/settings.py

SECRET_KEY='Ваш ключ'

для генерации ключа можно использовать сайт:

https://djecrety.ir/
```

Перейти в папку, в которой находится файл manage.py:

```
cd yatube_api/
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Системные требования

Версия Python:

```
Python 3.7
```

Зависимости:

```
Django==2.2.16
pytest==6.2.4
pytest-pythonpath==0.7.3
pytest-django==4.4.0
djangorestframework==3.12.4
djangorestframework-simplejwt==4.7.2
Pillow==8.3.1
PyJWT==2.1.0
requests==2.26.0
```

## Примеры
### Создание нового пользователя.

Запрос
```
POST http://127.0.0.1:8000/api/v1/users/
Content-Type: application/json

{
    "username": "example_user",
    "password": "1234_password"
}
```

Вернет
```
{
  "email": "",
  "username": "example_user",
  "id": 1
}
```
и создаст нового в пользователя в бд.

### Получение токена.

Запрос
```
POST http://127.0.0.1:8000/api/v1/jwt/create/
Content-Type: application/json

{
    "username": "example_user",
    "password": "1234_password"
}
```

Вернет токен в поле access ,а также refresh поле необходимое для обновления токена.
```
{
  "refresh": "example_refresh_field",
  "access": "example_access_field"
}
```

### Создание поста.

Запрос
```
POST http://127.0.0.1:8000/api/v1/posts/
Content-Type: application/json
Authorization: Bearer <token>

{
    "text": "example_text"
}
```

Вернет
```
{
  "id": 1,
  "text": "example_text",
  "author": "example_user",
  "image": null,
  "group": null,
  "pub_date": "2022-10-30T06:00:58.435119Z"
}
```
и создаст новый пост в бд.

### Возвращение списка постов.

Запрос
```
GET  http://127.0.0.1:8000/api/v1/posts/
Content-Type: application/json
Authorization: Bearer <token>
```

Вернет список всех пстов.
```
[
  {
    "id": 1,
    "text": "example_text",
    "author": "example_user",
    "image": null,
    "group": null,
    "pub_date": "2022-10-30T06:00:58.435119Z"
  },
  {
    "id": 2,
    "text": "example_text2",
    "author": "example_user",
    "image": null,
    "group": null,
    "pub_date": "2022-10-30T06:04:02.704151Z"
  }
]
```
Данный запрос поддерживает LimitOffset пагинацию.

### Подписка.

Запрос
```
POST http://127.0.0.1:8000/api/v1/follow/
Content-Type: application/json
Authorization: Bearer <token>

{
    "following": "example_user2"
}
```

Вернет
```
{
  "user": "example_user",
  "following": "example_user2"
}
```
И осществит подписку на пользователи указанного в поле following.
