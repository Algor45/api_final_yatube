### Описание
Данный проект является интерфейсом API для проекта yatube.

Аутентификация в проекте построена на **JWT-токенах**.

Неаутентифицированные пользователи имеют разрешение только на чтение.

Аутентифицированные пользователи могут создавать контент , а также изменять только свой контент.


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram.git
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

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
