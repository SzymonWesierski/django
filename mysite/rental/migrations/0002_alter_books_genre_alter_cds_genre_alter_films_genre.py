# Generated by Django 4.0.4 on 2022-06-05 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='genre',
            field=models.CharField(choices=[('Fantastyka', 'Fantastyka'), ('Sci–Fi', 'Sci–Fi'), ('Romans', 'Romans'), ('Horror', 'Horror'), ('Thriller', 'Thriller'), ('Historyczna', 'Historyczna')], max_length=30),
        ),
        migrations.AlterField(
            model_name='cds',
            name='genre',
            field=models.CharField(choices=[('Rock', 'Rock'), ('POP', 'POP'), ('Disco', 'Disco'), ('Rap', 'Rap'), ('Reggae', 'Reggae'), ('Blues', 'Blues')], max_length=50),
        ),
        migrations.AlterField(
            model_name='films',
            name='genre',
            field=models.CharField(choices=[('Fabularny', 'Fabularny'), ('Horror', 'Horror'), ('Romans', 'Romans'), ('Thriller', 'Thriller'), ('Sci–Fi', 'Sci–Fi'), ('Komedio-dramat', '')], max_length=30),
        ),
    ]