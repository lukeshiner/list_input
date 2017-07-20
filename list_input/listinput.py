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
        self.required = kwargs['required']
        super().__init__(*args, **kwargs)

    def validate(self, value):
        super().validate(value)
        try:
            json_value = json.loads(value)
        except ValueError:
            raise ValidationError('Not valid JSON.')
        if not isinstance(json_value, list):
            raise ValidationError('Not valid JSON list.')
        if self.minimum > 0 and len(json_value) < self.minimum:
            raise ValidationError(
                'At least {} value(s) required'.format(self.minimum))
        if self.maximum > 0 and len(json_value) > self.maximum:
            raise ValidationError(
                'No more than {} values can be supplied'.format(self.maximum))

    def clean(self, value):
        value = super().clean(value)
        return json.loads(value)
