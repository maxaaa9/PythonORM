import os
import django
from django.db.models import QuerySet, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


def create_pet(name: str, species: str) -> str:
    new_pet = Pet.objects.create(name=name, species=species)

    return f"{new_pet.name} is a very cute {new_pet.species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool) -> str:
    new_artifact = Artifact.objects.create(name=name,
                                           origin=origin,
                                           age=age,
                                           description=description,
                                           is_magical=is_magical)

    return f"The artifact {new_artifact.name} is {new_artifact.age} years old!"


def rename_artifact(artifact: Artifact, new_name: str) -> None:
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name


def delete_all_artifacts() -> None:
    Artifact.objects.all().delete()


def show_all_locations() -> str:
    my_locations = []
    for location in Location.objects.all().order_by("-id"):
        my_locations.append(f"{location.name} has a population of {location.population}!")

    return '\n'.join(my_locations)


def new_capital() -> None:
    new_capital = Location.objects.first()
    new_capital.is_capital = True
    new_capital.save()


def get_capitals() -> QuerySet:
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location() -> None:
    Location.objects.first().delete()


def apply_discount() -> None:
    all_cars = Car.objects.all()

    for car in all_cars:
        percentage = sum(int(x) for x in str(car.year)) / 100
        total_discount = float(car.price) * percentage
        car.price_with_discount = float(car.price) - total_discount
        car.save()


def get_recent_cars() -> QuerySet:
    cars = Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')
    return cars


def delete_last_car() -> None:
    Car.objects.last().delete()


def show_unfinished_tasks() -> str:
    incomplete_tasks = []
    for task in Task.objects.filter(is_finished=False):
        incomplete_tasks.append(f"Task - {task.title} needs to be done until {task.due_date}!")

    return '\n'.join(incomplete_tasks)


def complete_odd_tasks() -> None:
    # Task.objects.filter(int(id) % 2 != 0).update(is_finished=True)
    Task.objects.annotate(id_mod=F('id') % 2).filter(id_mod=1).update(is_finished=True)


def encode_and_replace(text: str, task_title: str) -> None:
    encoded_text = ''.join(chr(ord(x) - 3) for x in text)
    Task.objects.filter(title=task_title).update(description=encoded_text)


def get_deluxe_rooms() -> str:
    deluxe_rooms = []

    for room in HotelRoom.objects.filter(room_type='Deluxe'):
        if room.id % 2 == 0:
            deluxe_rooms.append(f"Deluxe room with number {room.room_number} costs {room.price_per_night}$ per night!")

    return '\n'.join(deluxe_rooms)


def increase_room_capacity() -> None:
    all_rooms = HotelRoom.objects.all().order_by('id')
    for index, room in enumerate(all_rooms):
        if room.is_reserved:
            if index == 0 and room.capacity is not None:
                all_rooms[index].capacity += int(room.id)
                continue

            all_rooms[index].capacity += int(all_rooms[index - 1].capacity)

    HotelRoom.objects.bulk_update(all_rooms, ['capacity'])


def reserve_first_room() -> None:
    first_room = HotelRoom.objects.first()
    if first_room:
        first_room.is_reserved = True
        first_room.save()


def delete_last_room() -> None:
    last_room = HotelRoom.objects.last()
    if last_room and not last_room.is_reserved:
        last_room.delete()


def update_characters() -> None:
    Character.objects.filter(class_name='Mage').update(level=F('level') + 3,
                                                       intelligence=F('intelligence') - 7)

    Character.objects.filter(class_name='Warrior').update(hit_points=F('hit_points') / 2,
                                                          dexterity=F('dexterity') + 4)

    Character.objects.filter(class_name__in=['Assassin', 'Scout']).update(inventory="The inventory is empty")


def fuse_characters(first_character: Character, second_character: Character) -> None:
    Character.objects.create(
        name=f"{first_character.name} {second_character.name}",
        class_name="Fusion",
        level=(first_character.level + second_character.level) // 2,
        strength=(first_character.strength + second_character.strength) * 1.2,
        dexterity=(first_character.dexterity + second_character.dexterity) * 1.4,
        intelligence=(first_character.intelligence + second_character.intelligence) * 1.5,
        hit_points=(first_character.hit_points + second_character.hit_points),
        inventory="Bow of the Elven Lords, Amulet of Eternal Wisdom"
        if first_character.class_name in ['Mage', 'Scout']
        else "Dragon Scale Armor, Excalibur"
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity() -> None:
    Character.objects.all().update(dexterity=30)


def grand_intelligence() -> None:
    Character.objects.all().update(intelligence=40)


def grand_strength() -> None:
    Character.objects.all().update(strength=50)


def delete_characters() -> None:
    Character.objects.filter(inventory="The inventory is empty").delete()

# Create queries within functions

# character1 = Character.objects.create(
#     name='Gandalf',
#     class_name='Mage',
#     level=10,
#     strength=15,
#     dexterity=20,
#     intelligence=25,
#     hit_points=100,
#     inventory='Staff of Magic, Spellbook',
# )
#
# character2 = Character.objects.create(
#     name='Hector',
#     class_name='Warrior',
#     level=12,
#     strength=30,
#     dexterity=15,
#     intelligence=10,
#     hit_points=150,
#     inventory='Sword of Troy, Shield of Protection',
# )
#
# fuse_characters(character1, character2)
# fusion = Character.objects.filter(class_name='Fusion').get()
#
# print(fusion.name)
# print(fusion.class_name)
# print(fusion.level)
# print(fusion.intelligence)
# print(fusion.inventory)









