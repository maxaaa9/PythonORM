import os
from typing import List

import django
from django.db.models import Case, When, Value, QuerySet

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal, Dungeon, Workout
from main_app.choices import OperationSystemChoice


# Create and check models


def show_highest_rated_art() -> str:
    art_name = ArtworkGallery.objects.all().order_by('-rating', 'id')[0]
    return f"{art_name.art_name} is the highest-rated art with a {art_name.rating} rating!"


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery) -> None:
    new_instances = [first_art, second_art]
    ArtworkGallery.objects.bulk_create(new_instances)


def delete_negative_rated_arts() -> None:
    ArtworkGallery.objects.filter(rating__lt=0).delete()


def show_the_most_expensive_laptop() -> str:
    laptop = Laptop.objects.order_by('-price', '-id').first()
    return f"{laptop.brand} is the most expensive laptop available for {laptop.price}$!"


def bulk_create_laptops(args: List[Laptop]) -> None:
    Laptop.objects.bulk_create(args)


def update_to_512_GB_storage() -> None:
    Laptop.objects.filter(brand__in=['Asus', 'Lenovo']).update(storage=512)


def update_to_16_GB_memory() -> None:
    Laptop.objects.filter(brand__in=['Apple', 'Dell', 'Acer']).update(memory=16)


def update_operation_systems() -> None:
    Laptop.objects.update(
        operation_system=Case(
            When(brand='Asus', then=Value('Windows')),
            When(brand='Apple', then=Value('MacOS')),
            When(brand__in=['Dell', 'Acer'], then=Value('Linux')),
            When(brand='Lenovo', then=Value('Chrome OS'))
        )
    )


def delete_inexpensive_laptops() -> None:
    Laptop.objects.filter(price__lt=1200).delete()


def bulk_create_chess_players(args: List[ChessPlayer]) -> None:
    ChessPlayer.objects.bulk_create(args)


def delete_chess_players() -> None:
    ChessPlayer.objects.filter(title='no title').delete()


def change_chess_games_won() -> None:
    ChessPlayer.objects.filter(title='GM').update(games_won=30)


def change_chess_games_lost() -> None:
    ChessPlayer.objects.filter(title='no title').update(games_lost=25)


def change_chess_games_drawn() -> None:
    ChessPlayer.objects.all().update(games_drawn=10)


def grand_chess_title_GM() -> None:
    ChessPlayer.objects.filter(rating__gte=2400).update(title="GM")


def grand_chess_title_IM() -> None:
    ChessPlayer.objects.filter(rating__range=(2300, 2399)).update(title="IM")


def grand_chess_title_FM() -> None:
    ChessPlayer.objects.filter(rating__range=(2200, 2299)).update(title="FM")


def grand_chess_title_regular_player() -> None:
    ChessPlayer.objects.filter(rating__range=(0, 2199)).update(title="regular player")


def set_new_chefs() -> None:
    Meal.objects.update(
        chef=Case(
            When(meal_type="Breakfast", then=Value("Gordon Ramsay")),
            When(meal_type="Lunch", then=Value("Julia Child")),
            When(meal_type="Dinner", then=Value("Jamie Oliver")),
            When(meal_type="Snack", then=Value("Thomas Keller")),
        )
    )


def set_new_preparation_times() -> None:
    Meal.objects.update(
        preparation_time=Case(
            When(meal_type="Breakfast", then=Value("10 minutes")),
            When(meal_type="Lunch", then=Value("12 minutes")),
            When(meal_type="Dinner", then=Value("15 minutes")),
            When(meal_type="Snack", then=Value("5 minutes")),
        )
    )


def update_low_calorie_meals() -> None:
    Meal.objects.filter(meal_type__in=("Breakfast", "Dinner")).update(calories=400)


def update_high_calorie_meals() -> None:
    Meal.objects.filter(meal_type__in=("Lunch", "Snack")).update(calories=700)


def delete_lunch_and_snack_meals() -> None:
    Meal.objects.filter(meal_type__in=("Lunch", "Snack")).delete()


def show_hard_dungeons() -> str:
    all_dungeons = []

    for dung in Dungeon.objects.filter(difficulty='Hard').order_by('-location'):
        all_dungeons.append(f"{dung.name} is guarded by {dung.boss_name} who has {dung.boss_health} health points!")

    return '\n'.join(all_dungeons)


def bulk_create_dungeons(args: List[Dungeon]) -> None:
    Dungeon.objects.bulk_create(args)


def update_dungeon_names() -> None:
    Dungeon.objects.update(
        name=Case(
            When(difficulty='Easy', then=Value("The Erased Thombs")),
            When(difficulty='Medium', then=Value("The Coral Labyrinth")),
            When(difficulty='Hard', then=Value("The Lost Haunt"))
        )
    )


def update_dungeon_bosses_health() -> None:
    Dungeon.objects.exclude(difficulty='Easy').update(boss_health=500)


def update_dungeon_recommended_levels() -> None:
    Dungeon.objects.update(
        recommended_level=Case(
            When(difficulty='Easy', then=Value(25)),
            When(difficulty='Medium', then=Value(50)),
            When(difficulty='Hard', then=Value(75)),
        )
    )


def update_dungeon_rewards() -> None:
    Dungeon.objects.filter(boss_health=500).update(reward="1000 Gold")
    Dungeon.objects.filter(location__startswith="E").update(reward="New dungeon unlocked")
    Dungeon.objects.filter(location__endswith="s").update(reward="Dragonheart Amulet")


def set_new_locations() -> None:
    Dungeon.objects.update(
        location=Case(
            When(recommended_level=25, then=Value("Enchanted Maze")),
            When(recommended_level=50, then=Value("Grimstone Mines")),
            When(recommended_level=75, then=Value("Shadowed Abyss")),
        )
    )


def show_workouts() -> str:
    workouts = []
    for workout in Workout.objects.filter(workout_type__in=['Calisthenics', 'CrossFit']).order_by('id'):
        workouts.append(f"{workout.name} from {workout.workout_type} type has {workout.difficulty} difficulty!")

    return '\n'.join(workouts)


def get_high_difficulty_cardio_workouts() -> QuerySet:
    return Workout.objects.filter(workout_type='Cardio', difficulty='High').order_by('instructor')


def set_new_instructors() -> None:
    Workout.objects.update(
        instructor=Case(
            When(workout_type='Cardio', then=Value('John Smith')),
            When(workout_type='Strength', then=Value('Michael Williams')),
            When(workout_type='Yoga', then=Value('Emily Johnson')),
            When(workout_type='CrossFit', then=Value('Sarah Davis')),
            When(workout_type='Calisthenics', then=Value('Chris Heria')),
        )
    )


def set_new_duration_times() -> None:
    Workout.objects.update(
        duration=Case(
            When(instructor='John Smith', then=Value('15 minutes')),
            When(instructor='Sarah Davis', then=Value('30 minutes')),
            When(instructor='Chris Heria', then=Value('45 minutes')),
            When(instructor='Michael Williams', then=Value('1 hour')),
            When(instructor='Emily Johnson', then=Value('1 hour and 30 minutes')),
        )
    )


def delete_workouts() -> None:
    Workout.objects.exclude(workout_type__in=["Strength", "Calisthenics"]).delete()


# Run and print your queries
# Create two Workout instances
workout1 = Workout.objects.create(
    name="Push-Ups",
    workout_type="Calisthenics",
    duration="10 minutes",
    difficulty="Intermediate",
    calories_burned=200,
    instructor="Bob"
)

workout2 = Workout.objects.create(
    name="Running",
    workout_type="Cardio",
    duration="30 minutes",
    difficulty="High",
    calories_burned=400,
    instructor="Lilly"
)

# Run the functions
print(show_workouts())

high_difficulty_cardio_workouts = get_high_difficulty_cardio_workouts()
for workout in high_difficulty_cardio_workouts:
    print(f"{workout.name} by {workout.instructor}")

set_new_instructors()
for workout in Workout.objects.all():
    print(f"Instructor: {workout.instructor}")

set_new_duration_times()
for workout in Workout.objects.all():
    print(f"Duration: {workout.duration}")














