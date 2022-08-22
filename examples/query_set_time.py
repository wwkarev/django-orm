from library.models import Book, Author, Category
from django.db import connection
from django.db.models import Q, Count


books = Book.objects.all()
books = books.filter(name='Стоик')
books = books.filter(publish_date='1947-01-01')

print(f"Количество запросов {len(connection.queries)}") # QuerySet "ленивы" кол-во запрсов 0

for book in books: # тут происходит запрос в базу
    print(f"{book.name} {book.publish_date}")

print(f"Количество запросов {len(connection.queries)}")

for book in books: # тут не будет запрса в базу, т.к. queryset не изменился, результат достается из кэша
    print(f"{book.name} {book.publish_date}")

print(f"Количество запросов {len(connection.queries)}")

books = books.order_by('name') # query_set изменился

for book in books: # тут происходит запрос в базу, т.к. queryset изменился, результат в кэше не аутуален
    print(f"{book.name} {book.publish_date}")

print(f"Количество запросов {len(connection.queries)}")
for query in connection.queries:
    print(query['sql'])