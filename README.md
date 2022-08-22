# Описание
В проекте представлены примеры работы с ORM.

# Установка
`python3.7 -m venv venv` - создание виртуального окружения

`source venv/bin/activate` - активация виртуального окружения

`pip install -r requierements.txt` - установка зависимостей

`python manage.py migrate` - применение миграций (создание таблиц в БД, добавление данных)

# Структура проекта
В директории examples представлены скрипты:
* filter_order_by.py - примеры where, order_by
* query_set_time.py - разбираем в какое время выполняется query_set
* create_update_delete.py - примеры операций создания, обновления, удаления
* select_prefetch_related.py - примеры использования select_related, prefetch_related
* mana_to_many.py - примеры работы с many_to_many связью, group by, count()

# Как рабоать с скриптами
Запуск скриптов производить через django shell:

`python manage.py shell < examples/many_to_many.py`

Примеры разбиты на блоки, предлагается раскомментировать интересующий блок и запустить код.