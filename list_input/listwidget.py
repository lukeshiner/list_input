from django import forms


class ListWidget(forms.TextInput):

    list_separator = ';'
    maximum = 0
    minimum = 0

    template_name = 'list_input/list_widget.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['separator'] = self.list_separator
        context['widget']['maximum'] = self.maximum
        context['widget']['minimum'] = self.minimum
        return context
