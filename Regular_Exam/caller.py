import os
import django
from django.db.models import Q, Count, Sum, Avg, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Astronaut, Spacecraft, Mission


def get_astronauts(search_string=None):
    if search_string is None:
        return ''

    astronauts = Astronaut.objects.filter(
        Q(phone_number__icontains=search_string) | Q(name__icontains=search_string)).order_by('name')

    if not astronauts:
        return ''

    astronauts_info = []
    for astronaut in astronauts:
        astronaut_active = 'Active' if astronaut.is_active else 'Inactive'
        astronauts_info.append(f"Astronaut: {astronaut.name}, "
                               f"phone number: {astronaut.phone_number}, "
                               f"status: {astronaut_active}")

    return '\n'.join(astronauts_info)


def get_top_astronaut():
    greatest_astronaut = Astronaut.objects.get_astronauts_by_missions_count()

    top_astronaut = greatest_astronaut.first()

    if top_astronaut and top_astronaut.total_missions > 0:
        return f"Top Astronaut: {top_astronaut.name} with {top_astronaut.total_missions} missions."
    else:
        return "No data."


def get_top_commander():
    commanders = Astronaut.objects.annotate(
        total_missions=Count('mission', filter=Q(mission__commander=F('pk')))
    ).order_by(
        '-total_missions', 'phone_number'
    )

    if not commanders or commanders[0].total_missions == 0:
        return "No data."

    top_commander = commanders[0]
    num_of_missions = top_commander.total_missions

    return f"Top Commander: {top_commander.name} with {num_of_missions} commanded missions."


def get_last_completed_mission():
    last_completed_mission = Mission.objects.filter(
        status='Completed'
    ).order_by('-launch_date').first()

    if not last_completed_mission:
        return "No data."

    commander_name = last_completed_mission.commander.name if last_completed_mission.commander else "TBA"

    astronaut_names = last_completed_mission.astronauts.order_by('name').values_list('name', flat=True)
    astronauts_list = ', '.join(astronaut_names)

    spacecraft_name = last_completed_mission.spacecraft.name

    total_spacewalks = last_completed_mission.astronauts.aggregate(
        total_spacewalks=Sum('spacewalks')
    )['total_spacewalks'] or 0

    result = (
        f"The last completed mission is: {last_completed_mission.name}. "
        f"Commander: {commander_name}. Astronauts: {astronauts_list}. "
        f"Spacecraft: {spacecraft_name}. Total spacewalks: {total_spacewalks}."
    )

    return result


def get_most_used_spacecraft():
    spacecrafts = Spacecraft.objects.prefetch_related('mission_set').annotate(
        total_missions=Count('mission')
    ).order_by(
        'name'
    )

    if not spacecrafts.exists():
        return "No data."

    most_used_spacecraft = spacecrafts[0]
    num_missions = most_used_spacecraft.total_missions

    num_astronauts = Mission.objects.filter(
        spacecraft=most_used_spacecraft
        ).values('astronauts').distinct().count()

    return (f"The most used spacecraft is: {most_used_spacecraft.name}, "
            f"manufactured by {most_used_spacecraft.manufacturer}, "
            f"used in {num_missions} missions, astronauts on missions: {num_astronauts}.")


def decrease_spacecrafts_weight():
    planned_missions = Mission.objects.filter(status='Planned')
    affected_spacecrafts = Spacecraft.objects.filter(mission__in=planned_missions).distinct()

    spacecrafts_to_update = affected_spacecrafts.filter(weight__gte=200.0)

    if not spacecrafts_to_update.exists():
        return "No changes in weight."

    num_spacecrafts_affected = spacecrafts_to_update.update(weight=F('weight') - 200.0)

    Spacecraft.objects.filter(weight__lt=0).update(weight=0.0)

    avg_weight = Spacecraft.objects.aggregate(Avg('weight'))['weight__avg']
    if avg_weight is None:
        avg_weight = 0.0

    avg_weight = round(avg_weight, 1)

    return (
        f"The weight of {num_spacecrafts_affected} spacecrafts has been decreased. "
        f"The new average weight of all spacecrafts is {avg_weight}kg"
    )

# Create queries within functions
