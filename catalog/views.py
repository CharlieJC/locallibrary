from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
# Create your views here.

# home page


def index(request):
    context = {
        'num_books': Book.objects.all().count(),
        'num_instances': BookInstance.objects.all().count(),
        'num_instances_available': BookInstance.objects.filter(status__exact='a').count(),
        'num_authors': Author.objects.count()
    }

    return render(request, 'index.html', context=context)

