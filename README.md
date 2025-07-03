# CSV Filter & Aggregator CLI Tool

Утилита командной строки на Python для **фильтрации** и **агрегации** данных из больших CSV-файлов с построчной обработкой.

## Возможности

-  Чтение CSV-файлов по частям
-  Фильтрация с множественными условиями (`--where`)
-  Агрегация (`avg`, `min`, `max`) по колонке (`--aggregate`)
-  Вывод в формате таблицы (`tabulate`)

---
## Структура проекта

Workmate/ /n
├── main.py /n
├── operations/ /n
│   ├── Base_operation.py /n
│   ├── Filter_operation.py /n
│   └── Aggregate_Operation.py /n
├── Utils.py /n
├── test/ /n
│   └── test_main.py /n
└── data/ /n
    └── products.csv /n
---

## Примеры исрользования 

## Поддерживамые операторы

Фильтрация:

=

>

<

>=

<=

Агрегация:

avg

min

max

## Фильтрация

```bash
python main.py --file data/products.csv --where "brand=apple" --where "rating>4"
python main.py --file data/products.csv --where "brand=apple"
```

## Анренация 

```bash
python main.py --file data/products.csv --aggregate "rating=avg"
```
## Фильтрация + Агрегация

```bash
python main.py --file data/products.csv --where "brand=apple" --aggregate "rating=max"
```

---

## Тесты

Тесты написаны с использованием pytest и pytest-cov.

## Запуск тестов

```bash
pytest --cov=main tests/test_main.py
```
