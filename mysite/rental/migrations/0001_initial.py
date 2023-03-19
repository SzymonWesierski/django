# Generated by Django 4.0.4 on 2022-06-05 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=30)),
                ('ISBN', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CDs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=30)),
                ('songs_list', models.CharField(max_length=1000)),
                ('duration', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=30)),
                ('duration', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rentals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserRentals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_data', models.DateField()),
                ('return_data', models.DateField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('book_rent', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rental.books')),
                ('cd_rent', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rental.cds')),
                ('film_rent', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rental.films')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='films',
            name='rental_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.rentals'),
        ),
        migrations.AddField(
            model_name='cds',
            name='rental_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.rentals'),
        ),
        migrations.AddField(
            model_name='books',
            name='rental_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.rentals'),
        ),
    ]
