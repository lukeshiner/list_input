"""ListWidget, the widget for ListInput."""

from django import forms


class ListWidget(forms.TextInput):
    """ListWidget is the default widget for the ListInput field."""

    list_separator = ';'
    maximum = 0
    minimum = 0

    template_name = 'list_input/list_widget.html'

    def get_context(self, name, value, attrs):
        """Return template context."""
        context = super().get_context(name, value, attrs)
        context['widget']['separator'] = self.list_separator
        context['widget']['maximum'] = self.maximum
        context['widget']['minimum'] = self.minimum
        return context
