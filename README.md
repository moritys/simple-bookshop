# simple-bookshop
🐛🍫💘

## сделать не букшоп, а сервис по аренде книг на время

#### Команды alembic для склерозных

1. Инициализация alembic в проекте:

```alembic init --template async alembic```

* *`--template async` для асинхронного шаблона*

2. Автогенерация миграций

```alembic revision --autogenerate -m "First migration"```

3. Выполнение всех неприменённых миграций

```alembic upgrade head```

4. Отмена миграций

```alembic downgrade base```

5. все миграции в хронологическом порядке

```alembic history```

* *`-v` в более подробном виде*
* *`-i` вывести метку актуальной миграции*

6. Посмотреть последнюю применённую миграцию

```alembic current```

7. 