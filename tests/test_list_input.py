import json

import pytest
from django.core.exceptions import ValidationError

from list_input import ListInput


def test_prepare_value():
    field = ListInput()
    prepare_value = field.prepare_value(["One", "Two", "Three"])
    assert prepare_value == '["One", "Two", "Three"]'


def test_to_python():
    field = ListInput()
    python_value = field.to_python('["One", "Two", "Three"]')
    assert python_value == ["One", "Two", "Three"]


def test_below_minimum_raises():
    with pytest.raises(ValidationError):
        ListInput(minimum=1).clean(json.dumps([]))


def test_no_minimum_does_not_raise():
    ListInput(minimum=0, required=False).clean(json.dumps([]))


def test_above_maximum_raises():
    with pytest.raises(ValidationError):
        ListInput(maximum=1).clean(json.dumps(["One", "Two", "Three"]))


def test_no_maximum_does_not_raise():
    ListInput(maximum=0).clean(json.dumps(["One" for i in range(200)]))


def test_required():
    with pytest.raises(ValidationError):
        ListInput(required=True).clean(json.dumps([]))
