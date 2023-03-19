from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Deferrable, UniqueConstraint
from django.core.exceptions import ValidationError

# Create your models here.

class Rentals(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name + ", " + self.address


def ISBN_validation(ISBN):
    if len(ISBN) != 13:
        raise ValidationError('ISBN must be 13 characters long ')
    else:
        return ISBN


class Books(models.Model):
    book_genre = (
        ('Fantastyka','Fantastyka'),
        ('Sci–Fi','Sci–Fi'),
        ('Romans','Romans'),
        ('Horror','Horror'),
        ('Thriller','Thriller'),
        ('Historyczna','Historyczna')
    )

    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=30, choices=book_genre)
    ISBN = models.CharField(max_length=30, unique=True, validators=[ISBN_validation])
    slug = models.SlugField(max_length=255, unique=True)
    rental_id = models.ForeignKey(Rentals, on_delete=models.CASCADE)
    #deposited_by = models.ManyToManyField(User, through='UserRentals', blank=True)

    class Meta:
        verbose_name_plural = 'Books'
        ordering = ('-id',)
        constraints = [
            models.UniqueConstraint(fields = ['title','author','genre'], name = 'unique_book')
        ]

    def __str__(self):
        return self.author + ", " + self.title

    def get_absolute_url(self):
        return reverse('rental:index')


class Films(models.Model):
    film_genre = (
        ('Fabularny', 'Fabularny'),
        ('Horror', 'Horror'),
        ('Romans', 'Romans'),
        ('Thriller', 'Thriller'),
        ('Sci–Fi', 'Sci–Fi'),
        ('Komedio-dramat', '')
    )

    director = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=30, choices=film_genre)
    duration = models.CharField(max_length=30)
    slug = models.SlugField(max_length=255, unique=True)
    rental_id = models.ForeignKey(Rentals, on_delete=models.CASCADE)
    #deposited_by = models.ManyToManyField(User, through='UserRentals', blank=True)

    class Meta:
        verbose_name_plural = 'Films'
        ordering = ('-id',)
        constraints = [
            models.UniqueConstraint(fields = ['title','director','duration'], name = 'unique_film')
        ]

    def __str__(self):
        return self.director + ", " + self.title

    def get_absolute_url(self):
        return reverse('rental:filmIndex')


class CDs(models.Model):
    music_genre = (
        ('Rock', 'Rock'),
        ('POP', 'POP'),
        ('Disco', 'Disco'),
        ('Rap', 'Rap'),
        ('Reggae', 'Reggae'),
        ('Blues', 'Blues')
    )

    band = models.CharField(max_length=50)
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=50, choices=music_genre)
    songs_list = models.CharField(max_length=1000)
    duration = models.CharField(max_length=30)
    slug = models.SlugField(max_length=255, unique=True)
    rental_id = models.ForeignKey(Rentals, on_delete=models.CASCADE)
    #deposited_by = models.ManyToManyField(User, through='UserRentals', blank=True)

    def __str__(self):
        return self.band + ", " + self.title

    def get_absolute_url(self):
        return reverse('rental:cdIndex')

#jeszcze klienci i wypozyczenia

class UserRentals(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_rent = models.OneToOneField(Books, null = True, blank = True, on_delete = models.CASCADE)
    film_rent = models.OneToOneField(Films, null = True, blank = True, on_delete = models.CASCADE)
    cd_rent = models.OneToOneField(CDs, null = True, blank = True, on_delete = models.CASCADE)
    rent_data = models.DateField()
    return_data = models.DateField()
    slug = models.SlugField(max_length=255, unique=True)

    def get_absolute_url(self):
        return reverse('rental:index')

    def __str__(self):
        string = ""
        if self.book_rent is not None:
            string += self.book_rent.title
        if self.cd_rent is not None:
            string += self.cd_rent.title
        if self.film_rent is not None:
            string += self.film_rent.title


        return "User: " + self.user_id.username + ", rent: " + string