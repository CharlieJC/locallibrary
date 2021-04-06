from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic


# Create your views here.

# home page


def index(request):
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': Book.objects.all().count(),
        'num_instances': BookInstance.objects.all().count(),
        'num_instances_available': BookInstance.objects.filter(status__exact='a').count(),
        'num_authors': Author.objects.count(),
        'num_visits': num_visits,
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


class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'
    template_name = 'authors/authorlist.html'
    paginate_by = 2

    def get_queryset(self):
        return Author.objects.all()[:5]


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'authors/detail.html'
