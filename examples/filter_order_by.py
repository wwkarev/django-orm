from library.models import Book, Author, Category
from django.db import connection
from django.db.models import Q, Count


# select * from library_book;
books = Book.objects.all()

# select * from library_book where publish_date = '1947-01-01';
# books = Book.objects.filter(publish_date='1947-01-01')


# select * from library_book where publish_date != '1947-01-01';
# books = Book.objects.exclude(publish_date='1947-01-01')


# select * from library_book where publish_date = '1947-01-01' and name = 'Стоик';
# books = Book.objects.filter(publish_date='1947-01-01', name='Стоик') # 1 способ
# books = Book.objects.filter(publish_date='1947-01-01').filter(name='Стоик') # 2 способ 


# select * from library_book where publish_date >= '1947-01-01';
# __gt - >
# __lt - <
# __gte - >=
# __lte - <=
# books = Book.objects.filter(publish_date__gte='1947-01-01')


# select * from library_book where name LIKE 'Б%';
# books = Book.objects.filter(name__startswith='Б')


# select * from library_book where publish_date = '1912-01-01' or publish_date >= '1947-01-01';
# books = Book.objects.filter(Q(publish_date='1912-01-01') | Q(publish_date__gte='1947-01-01'))


# select * from library_book order by publish_date;
# books = Book.objects.order_by("-publish_date")


# select * from library_book where publish_date >= '1900-01-01' order by name;
# books = Book.objects.filter(publish_date__gte='1900-01-01').order_by('name')

# select b.* from library_book b inner join library_author a on b.author_id = a.id where a.last_name = "Драйзер";
# books = Book.objects.filter(author__last_name="Драйзер") 
# select a.*, b.* from library_book b inner join library_author a on b.author_id = a.id where a.last_name = "Драйзер";
# books = Book.objects.select_related("author").filter(author__last_name="Драйзер") 

for book in books:
    print(f"{book.name} {book.publish_date}")
for query in connection.queries:
    print(query['sql'])