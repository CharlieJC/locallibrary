from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic
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

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/booklist.html'
    paginate_by = 2

    def get_queryset(self):
        return Book.objects.all()[:5]

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'
