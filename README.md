
# Калькулятор банковского вклада

REST API сервис для мгновенного расчета ежемесячного дохода по банковскому вкладу




## API Reference 

#### Request

Для работы сервиса пользователю необходимо отправить `POST` - запрос на адрес:

```
  http://127.0.0.1:8000/deposit
```
С параметрами в теле запроса:

| Parameter | Type      | Validation          | Description                  |
| :-------- | :-------- | :------------------ | :--------------------------- |
| `date`    | `string`  | dd.mm.YYY           | Дата подачи заявки           |
| `periods` | `integer` | 1 to 60             | Количество месяцев по вкладу |
| `amount`  | `integer` | 10_000 to 3_000_000 | Сумма вклада                 |
| `rate`    | `float`   | 1 to 8              | Процент по вкладу            |

Например:

```
{
    "date": "30.01.2024",
    "periods": 3,
    "amount": 10000,
    "rate": 6
}
```

#### Response

В теле ответа пользователю придёт таблица, состоящая из ежемесячных дат начисления процента и суммой на каждую дату:

```
{
    "30.01.2024": 10050.0,
    "29.02.2024": 10100.25,
    "30.03.2024": 10150.75
}
```


## Запуск проекта

### Запуск локально на Windows

1. Клонировать проект из репозитория GitHub:
```
  git clone git@github.com:ZubovEvgeniy/deposit_calc.git
```

2. Установить виртуальное окружение
```
  python -m venv venv
```

3. Активировать виртуальное окружение
```
  source venv/Scripts/activate
```

4. Обновить pip
```
  python -m pip install --upgrade pip
```

5. Установить зависимости
```
  cd deposit_calc
```
```
  pip install -r requirements.txt
```

6. Запустить проект
```
  python manage.py runserver
```

### Запуск на сервере из контейнера Docker

1. Клонировать проект из репозитория GitHub:
```
  git clone git@github.com:ZubovEvgeniy/deposit_calc.git
```

2. Собрать образ проекта
```
  sudo docker build -t deposit_calc . 
```
3. Запустить контейнер из образа
```
  sudo cd deposit_calc
```
```
  sudo docker run --name deposit_calc -it -p 8000:8000 deposit_calc
```

### Запуск на сервере из образа [DockerHub](https://hub.docker.com/)

1. Клонировать образ из DockerHub
```
  sudo docker pull evgeniyzubov/deposit_calc:v1.0
```

2. Запустить контейнер из образа
```
  sudo docker run --name deposit_calc -it -p 8000:8000 evgeniyzubov/deposit_calc:v1.0
```
## Технологии

* Python 3.8
* Django 4.1.7
* DRF 3.14.0


## Authors

- [Зубов Евгений](https://github.com/ZubovEvgeniy)

