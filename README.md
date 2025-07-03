# CSV Filter & Aggregator CLI Tool

Утилита командной строки на Python для **фильтрации** и **агрегации** данных из больших CSV-файлов с построчной обработкой.

## Возможности

-  Чтение CSV-файлов по частям
-  Фильтрация с множественными условиями (`--where`)
-  Агрегация (`avg`, `min`, `max`) по колонке (`--aggregate`)
-  Вывод в формате таблицы (`tabulate`)

---
## Структура проекта

Workmate/  
├── main.py  
├── operations/  
│   ├── Base_operation.py  
│   ├── Filter_operation.py  
│   └── Aggregate_Operation.py  
├── Utils.py  

├── test/  
│   └── test_main.py  
└── data/  
    └── products.csv  
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
