from django.core.exceptions import ValidationError


def validate_name_only_letters_and_space(value):
    for i in value:
        if not (i.isalpha() or i.isspace()):
            raise ValidationError('Name can only contain letters and spaces')


