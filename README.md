# Blog

**Blog на Django со следующим функционалом:**

- Реализован личный кабинет. Изменен пользователь с помощью AbstractBaseUser
- CRUD постов
- Комментирование постов
- Добавление постов в избранное 
- Подписка на рассылку по email с помощью [Celery](https://docs.celeryq.dev/en/stable/)
- Восстановление пароля

## Настройка

Склонируйте проект:
```
git clone https://github.com/Ramil2003/Blog.git
```

Создайте виртуальное окружение:
```
python3 -m venv venv
```

Активируйте вирт. окружение:
```
source venv/bin/activate
```

Установите зависимости:
```
pip install -r requirements.txt
```

Запустите docker-compose:
```
docker-compose up --build
```
