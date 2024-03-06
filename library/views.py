from django.shortcuts import render

from library.models import Book


def library_view(request):
    return render(request,"library/library_page.html" )


 def  books_view(request):
     books = Book.objects.all()
     return render(request,"library/books_list_html", {"books":books})