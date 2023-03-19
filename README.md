# Zadanie: Staromodna wypożyczalnia: Django

| Termin oddania | Punkty     |
|----------------|:-----------|
|    12.06.2021 23:00 |   30        |

--- 
Przekroczenie terminu o **n** zajęć wiąże się z karą:
- punkty uzyskania za realizację zadania są dzielone przez **2<sup>n</sup>**.

--- 
Bazując na [tutorialu do Django](https://docs.djangoproject.com/pl/4.0/intro/tutorial01/), 
napisać własną aplikację web spełniającą następujące warunki:

### Specyfikacja wymagań klienta
Klient prowadzi staromodną sieć wypożyczalni, w której można wypożyczać:
- książki charakteryzowane przez:
    - autora
    - tytuł
    - gatunek
    - ISBN
    - ID w wypożyczalni
  
- filmy opisane przez:
    - reżysera
    - tytuł
    - gatunek
    - czas trwania
    - ID w wypożyczalni
    
- płyty CD
    - zespół
    - tytuł
    - gatunek
    - lista utworów
    - czas trwania
    - ID w wypożyczalni

Wypożyczalnie posiadają:
- ID
- nazwę
- adres

Aplikacja ma dostarczać funkcjonalność umożliwiającą zalogowanym użytkownikom pełną edycję
posiadanych elementów do wypożyczenia. 
Edycja powinna zapewniać następujące reguły poprawności:
- książki:
    - wszystkie ISBN są różne
    - krotki: (autor, tytuł i gatunek)  nie mogą się powtarzać
  
- filmy:
    - liczby różnych filmów danego gatunku w ramach całej kolekcji mogą różnić się o 3
    - jeżeli reżyser i tytuł się powtarza, to czas trwania musi się różnić
    
- płyty CD:
    - w ramach jednego gatunku nie możemy oferować dwóch płyt o tej samej liście utworów
    - płyty danego zespołu mogą być oferowane tylko w dwóch gatunkach
    
Aplikacja przechowuje liczby poszczególnych elementów do wypożyczania oraz dane wypożyczających i 
ich dane o wypożyczeniach i zwrotach wypożyczanych elementów.

Aplikacja powinna również oferować statystyki wypożyczeń w zadanych odcinkach czasu:
- popularność książek, filmów i płyt w podziale na gatunki
- jednolity ranking wypożyczających w podziale na rodzaj i gatunek wypożyczanego elementy.

### Ograniczenia techniczne
1. Dane aplikacji powinny być utrwalane w bazie danych.
1. Wykorzystać mechanizm migracji bazy danych.
1. Aplikacja powinna być wytworzona w technologii Django z wykorzystaniem *Class-based views*.
1. Operacje powinny realizować pełen CRUD na danych programu.
1. Aplikacja (prócz panelu administratora) powinna udostępniać logowanie użytkowników w apliokacji.

### Punktacja
- **[10 punktów]** Modele danych, ich walidacja i mechanizm migracji danych.
- **[10 punktów]** CRUD adekwatny do treści zadania wykorzystujący *Class-based views*.
- **[5 punktów]** Logowanie i uprawnienia użytkowników do widoków.
- **[5 punktów]** Prezentacja statystyk.
