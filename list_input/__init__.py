"""
The List Input package provides a django input for multiple values.

It displays as a normal input. When a value is entered a new input appears
below it, so there is always a blank field for a new value.

It returns input values as a delimited list. The delimiter defaults to '|'
but can be configured to any character.

"""

from .listinput import ListInput  # NOQA
from .listwidget import ListWidget  # NOQA
