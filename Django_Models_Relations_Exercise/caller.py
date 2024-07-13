import os
from datetime import timedelta, date

import django
from django.db.models import QuerySet

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Book, Artist, Song, Product, Review, DrivingLicense, Driver, Owner, Registration, \
    Car


# Create queries within functions


def show_all_authors_with_their_books() -> str:
    all_authors_with_books = []
    for author in Author.objects.order_by('id'):
        author_books = Book.objects.filter(author=author)

        if not author_books:
            continue

        book_titles = ', '.join(b.title for b in author_books)
        all_authors_with_books.append(f"{author.name} has written - {book_titles}!")

    return '\n'.join(all_authors_with_books)


def delete_all_authors_without_books() -> None:
    Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str) -> QuerySet:
    # artist = Artist.objects.filter(name=artist_name).first().songs.all().order_by('-id')
    return Song.objects.filter(artists__name=artist_name).order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str) -> float:
    products = Review.objects.filter(product__name=product_name)
    average_rating = sum(p.rating for p in products) / products.count()
    return average_rating


def get_reviews_with_high_ratings(threshold: int) -> 'Product':
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews() -> 'Product':
    return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews() -> None:
    Product.objects.filter(reviews__isnull=True).delete()


def calculate_licenses_expiration_dates() -> str:
    expiration_date = 365

    licenses = []
    for l in DrivingLicense.objects.all().order_by('-license_number'):
        licenses.append(f"License with number: {l.license_number} expires on "
                        f"{l.issue_date + timedelta(days=expiration_date)}!")

    return '\n'.join(licenses)


def get_drivers_with_expired_licenses(due_date: date) -> QuerySet[Driver]:
    return Driver.objects.filter(license__issue_date__gt=due_date - timedelta(days=365))


def register_car_by_owner(owner: Owner) -> str:
    empty_registration = Registration.objects.filter(registration_date__isnull=True).first()
    non_registered_car = Car.objects.filter(registration__isnull=True).first()

    non_registered_car.owner = owner
    non_registered_car.save()

    empty_registration.registration_date = date.today()

    empty_registration.car = non_registered_car
    empty_registration.save()

    return (f"Successfully registered {non_registered_car.model} to "
            f"{owner.name} with registration number {empty_registration.registration_number}.")


# Test your code below


owner1 = Owner.objects.create(name='Ivelin Milchev')
owner2 = Owner.objects.create(name='Alice Smith')


car1 = Car.objects.create(model='Citroen C5', year=2004)
car2 = Car.objects.create(model='Honda Civic', year=2021)


registration1 = Registration.objects.create(registration_number='TX0044XA')
registration2 = Registration.objects.create(registration_number='XYZ789')
print(register_car_by_owner(owner1))
