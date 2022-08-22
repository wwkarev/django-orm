from library.models import Book, Author, Category
from django.db import connection
from django.db.models import Q, Count


# Добавляем новые категории книге
category_1 = Category.objects.create(name="Американская классика")
category_2 = Category.objects.create(name="Лучшее 20-й век")
book = Book.objects.get(name="Стоик")
book.categories.add(category_1)
book.categories.add(category_2)


# books = Book.objects.select_related('author').prefetch_related('categories').all() # many_to_many вытяггиваем через prefetch_related()
# for book in books:
#     author = book.author
#     print(f"{book.name} {book.publish_date} {author.first_name} {author.last_name}")
#     for category in book.categories.all():
#         print(f"Категория {category.name}")

# select select count(b.id), a.first_name, a.last_name from library_book b inner join library_author a on b.author_id = a.id group by a.first_name, a.last_name having count(b.id) > 1;
# authors = Author.objects.values('first_name', 'last_name').annotate(book_count=Count("books")).filter(book_count__gt=1)
# for author in authors:
#     print(f"{author['first_name']} {author['last_name']} {author['book_count']}")

print(f"Количество запросов {len(connection.queries)}")
for query in connection.queries:
    print(query['sql'])