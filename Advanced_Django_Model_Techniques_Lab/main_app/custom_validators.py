from django.core.exceptions import ValidationError


def validate_menu_categories(value) -> None:
    available_categories = ('Appetizers', 'Main Course', 'Desserts')
    for categories in available_categories:
        if categories not in value:
            raise ValidationError('The menu must include each of the categories "Appetizers", "Main Course", "Desserts".')

