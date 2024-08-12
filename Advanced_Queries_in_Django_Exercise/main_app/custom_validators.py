from django.core.exceptions import ValidationError


class ValueInRangeValidator:
    def __init__(self, min_value: int, max_value: int, message=None):
        self.min_value = min_value
        self.max_value = max_value
        self.message = message

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        if value is None:
            self._message = f"The rating must be between {self.min_value:.1f} and {self.max_value:.1f}"

        else:
            self._message = value

    def __call__(self, value):
        if not self.min_value <= value <= self.max_value:
            raise ValidationError(self.message)

    def deconstruct(self):
        return ('main_app.custom_validators.ValueInRangeValidator',
                [self.min_value, self.max_value],
                {'message': self.message},
                )
