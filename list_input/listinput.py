import json

from django import forms
from django.core.exceptions import ValidationError

from . listwidget import ListWidget


class ListInput(forms.CharField):

    widget = ListWidget
    minimum = 0
    maximum = 0
    required = False

    def __init__(self, *args, **kwargs):
        if 'widget' in kwargs:
            self.widget = kwargs.pop('widget')
        if 'minimum' in kwargs:
            self.minimum = kwargs.pop('minimum')
        if 'maximum' in kwargs:
            self.maximum = kwargs.pop('maximum')
        self.widget.maximum = self.maximum
        self.widget.minimum = self.minimum
        self.required = kwargs.get('required', True)
        super().__init__(*args, **kwargs)

    def prepare_value(self, value):
        if isinstance(value, list):
            return json.dumps(value)
        return value

    def to_python(self, value):
        value = super().to_python(value)
        try:
            python_value = json.loads(value)
        except ValueError:
            raise ValidationError('Not valid JSON.')
        return python_value

    def validate(self, value):
        if self.minimum > 0 and len(value) < self.minimum:
            raise ValidationError(
                'At least {} value(s) required'.format(self.minimum))
        if self.maximum > 0 and len(value) > self.maximum:
            raise ValidationError(
                'No more than {} values can be supplied'.format(self.maximum))
