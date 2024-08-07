import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import RealEstateListing, VideoGame, BillingInfo, Invoice, Programmer, Technology, Project

# Run and print your queries
# Create instances of Technology
# tech1 = Technology.objects.create(name="Python", description="A high-level programming language")
#
# tech2 = Technology.objects.create(name="JavaScript", description="A scripting language for the web")
#
# tech3 = Technology.objects.create(name="SQL", description="Structured Query Language")
#
# # Create instances of Project
# project1 = Project.objects.create(name="Web App Project", description="Developing a web application")
#
# project1.technologies_used.add(tech1, tech2)
#
# project2 = Project.objects.create(name="Database Project", description="Managing databases")
#
# project2.technologies_used.add(tech3)
# # Create instances of Programmer
# programmer1 = Programmer.objects.create(name="Alice")
# programmer2 = Programmer.objects.create(name="Bob")
# # Associate projects with programmers
# programmer1.projects.add(project1, project2)
# programmer2.projects.add(project1)
# Execute the "get_programmers_with_technologies" method for a specific project
specific_project = Project.objects.get(name="Web App Project")
programmers_with_technologies = specific_project.get_programmers_with_technologies()

# Iterate through the related programmers and technologies
for programmer in programmers_with_technologies:
    print(f"Programmer: {programmer.name}")
    for technology in programmer.projects.get(name="Web App Project").technologies_used.all():
        print(f"- Technology: {technology.name}")

# Execute the "get_projects_with_technologies" method for a specific programmer
specific_programmer = Programmer.objects.get(name="Alice")
projects_with_technologies = specific_programmer.get_projects_with_technologies()

# Iterate through the related projects and technologies
for project in projects_with_technologies:
    print(f"Project: {project.name} for {specific_programmer.name}")
    for technology in project.technologies_used.all():
        print(f"- Technology: {technology.name}")



