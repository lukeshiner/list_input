"""The ListInput class."""

import json

from django import forms
from django.core.exceptions import ValidationError

from .listwidget import ListWidget


class ListInput(forms.CharField):
    """ListInput allows multiple values to be entered in a form field."""

    widget = ListWidget
    minimum = 0
    maximum = 0
    required = False

    def __init__(self, *args, **kwargs):
        """
        Create ListInput.

        Kwargs:
            widget:
                The widget to use to display the input. Optional but if passed
                must be None or an instance of listinput.ListWidget.
            minimum:
                The minimum number of values that can be input. If this
                argument is not passed the field can be blank. Otherwise
                entering fewer values will raise a ValidationError.
            maximum:
                The maximum number of values that can be input. Once this
                number of inputs has been entered no new input fields will
                appear. If a for is submitted with this value exceeded it will
                raise a ValidationError.
        """
        if "widget" in kwargs:
            self.widget = kwargs.pop("widget")
        if "minimum" in kwargs:
            self.minimum = kwargs.pop("minimum") or self.__class__.minimum
        if "maximum" in kwargs:
            self.maximum = kwargs.pop("maximum") or self.__class__.maximum
        self.required = kwargs.get("required", self.required)
        if self.minimum == 0 and self.required is True:
            self.minimum = 1
        self.widget.maximum = self.maximum
        self.widget.minimum = self.minimum
        super().__init__(*args, **kwargs)

    def prepare_value(self, value):
        """Return value as a JSON string."""
        if isinstance(value, list):
            return json.dumps(value)
        return value

    def to_python(self, value):
        """Return value as a list of strings."""
        value = super().to_python(value)
        if not value:
            return []
        try:
            python_value = json.loads(value)
        except ValueError:
            raise ValidationError('"{}" is not valid JSON.'.format(value))
        return python_value

    def validate(self, value):
        """
        Validate input.

        Raises:
            ValueError: If the number of values submitted is less than
            self.minumum or greater than self.maximum.

        """
        if self.minimum > 0 and len(value) < self.minimum:
            raise ValidationError("At least {} value(s) required".format(self.minimum))
        if self.maximum > 0 and len(value) > self.maximum:
            raise ValidationError(
                "No more than {} values can be supplied".format(self.maximum)
            )
