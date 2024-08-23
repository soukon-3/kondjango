
from django.http import JsonResponse
from .models import Book

def bye_world(request):
    # Bookモデルの全てのオブジェクトを取得
    books = Book.objects.all()

    # オブジェクトをリストとして整形し、辞書として返す
    books_data = list(books.values())

    return JsonResponse({'books': books_data})

