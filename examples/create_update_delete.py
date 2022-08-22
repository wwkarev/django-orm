from library.models import Book, Author, Category
from django.db import connection
from django.db.models import Q, Count

# Создание новой записи
new_author = Author.objects.create(first_name='Антон', last_name='Чехов', birthday='1860-01-17')

# Обновление записи
# author = Author.objects.get(first_name='Антон', last_name='Чехов')
# author.first_name = "Антонио"
# author.last_name = "Чехофф"
# author.save()

# author = Author.objects.get(first_name='Антонио', last_name='Чехофф')
# author.delete()

for author in Author.objects.all():
    print(f"{author.first_name} {author.last_name} {author.birthday}")