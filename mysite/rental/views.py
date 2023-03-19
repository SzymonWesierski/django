from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Rentals, Books, Films, CDs, UserRentals
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, View
from django.urls import reverse_lazy
from django.db.models import Count




class RentalsView(ListView):
    model = UserRentals
    template_name = "rental/rents.html"


class BooksView(ListView):
    model = Books
    template_name = "rental/index.html"


class FilmsView(ListView):
    model = Films
    template_name = "rental/filmIndex.html"


class CDsView(ListView):
    model = CDs
    template_name = "rental/cdIndex.html"


class addRentals(CreateView):
    model = UserRentals
    fields = '__all__'
    template_name = 'rental/add.html'


class addBook(CreateView):
    model = Books
    fields = '__all__'
    template_name = 'rental/add.html'


class addfilm(CreateView):
    model = Films
    fields = '__all__'
    template_name = 'rental/add.html'


class addcd(CreateView):
    model = CDs
    fields = '__all__'
    template_name = 'rental/add.html'


class updateBook(UpdateView):
    model = Books
    fields = '__all__'
    template_name = 'rental/update.html'


class updateFilm(UpdateView):
    model = Films
    fields = '__all__'
    template_name = 'rental/update.html'


class updateCD(UpdateView):
    model = CDs
    fields = '__all__'
    template_name = 'rental/update.html'


class updateRentals(UpdateView):
    model = UserRentals
    fields = '__all__'
    template_name = 'rental/update.html'


class deleteCD(DeleteView):
    model = CDs
    template_name = 'rental/delete.html'
    success_url = reverse_lazy("rental:index")


class deleteBook(DeleteView):
    model = Books
    template_name = 'rental/delete.html'
    success_url = reverse_lazy("rental:index")


class deleteFilm(DeleteView):
    model = Films
    template_name = 'rental/delete.html'
    success_url = reverse_lazy("rental:index")


class deleteRentals(DeleteView):
    model = UserRentals
    template_name = 'rental/delete.html'
    success_url = reverse_lazy("rental:index")

class formStat(View):
    def get(self, request):
        return render(request, 'rental/infostat.html')

def statchoice(request):
    if request.method == 'POST':
        choice = request.POST['chosen']
        date_from_str = request.POST['date_from']
        date_to_str =  request.POST['date_to']
        date_from = datetime.strptime(date_from_str, "%Y-%m-%d")
        date_to = datetime.strptime(date_to_str, "%Y-%m-%d")

        if date_to < date_from:
            messages.info(request, 'Date to must be newer than date from or at least equal')
            return HttpResponseRedirect("statchoice")

        else:
            if choice == "popularity":
                rentbook = list(Books.objects.annotate(Count('title')))
                rentcd = list(CDs.objects.annotate(Count('title')))
                rentfilm = list(Films.objects.annotate(Count('title')))

                context= {
                    'book': rentbook,
                    'cd':rentcd,
                    'film':rentfilm
                }
                return render(request, 'rental/statpopularity.html', context)

            if choice == "users":
                context = {
                    'rent': "Szymon"
                }
                return render(request, 'rental/statusers.html', context)
    else:
        return HttpResponseRedirect("formStat")






