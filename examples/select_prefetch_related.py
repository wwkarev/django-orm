from library.models import Book, Author, Category
from django.db import connection
from django.db.models import Q, Count


# select * from library_book; и много запросов на получение авторов.
books = Book.objects.all()
for book in books:
    author = book.author
    print(f"{book.name} {book.publish_date} {author.first_name} {author.last_name}")

# select a.* b.* from library_book b inner join library_author a on b.author_id = a.id; - вытягиваем все данные с помощью select_related
# books = Book.objects.select_related('author').all()
# for book in books:
#     author = book.author
#     print(f"{book.name} {book.publish_date} {author.first_name} {author.last_name}")

# author = Author.objects.get(first_name='Теодор', last_name='Драйзер')
# for book in author.books.all(): # Можем обратится к атрибуту books и получить все книги которые ссылаются на данного автора. books - это related_name из модели Book
#    print(f"{book.name} {book.publish_date} {author.first_name} {author.last_name}")


# author = Author.objects.get(first_name='Теодор', last_name='Драйзер')
# for book in author.books.all(): # Можем обратится к атрибуту books и получить все книги которые ссылаются на данного автора. books - это related_name из модели Book
#    print(f"{book.name} {book.publish_date} {author.first_name} {author.last_name}")


# for author in Author.objects.all():
#     for book in author.books.all(): # запрашиваем в БД книги для каждого автора
#         print(f"{book.name} {book.publish_date} {author.first_name} {author.last_name}")    

# for author in Author.objects.prefetch_related("books").all():
#     for book in author.books.all(): # prefetch_related - вытянул данные заранее
#         print(f"{book.name} {book.publish_date} {author.first_name} {author.last_name}")  


print(f"Количество запросов {len(connection.queries)}")
for query in connection.queries:
    print(query['sql'])