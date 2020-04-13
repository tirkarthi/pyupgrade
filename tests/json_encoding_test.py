import pytest

from pyupgrade import _fix_py3_plus


@pytest.mark.parametrize(
    's',
    [
        'json.loads({"a": 1})',
        'json.loads(open("foo.txt", encoding="utf-8").read(), cls=encoding)'
    ],
    ids=['simple json.loads', 'open with encoding']
)
def test_fix_json_loads_noop(s):
    assert _fix_py3_plus(s) == s


@pytest.mark.parametrize(
    's,expected',
    [
        (
            'json.loads(json.dumps({"a": 1}), encoding="utf-8")',
            'json.loads(json.dumps({"a": 1}))'
        ),
        (
            'json.loads(open("foo.txt", encoding="utf-8").read(), cls=encoding, encoding="utf-8")',
            'json.loads(open("foo.txt", encoding="utf-8").read(), cls=encoding)'
        ),
        (
            'json.loads(open("foo.txt", encoding="utf-8").read(), object_hook=Foo, encoding="utf-8", cls=encoding)',
            'json.loads(open("foo.txt", encoding="utf-8").read(), object_hook=Foo, cls=encoding)'
        )

    ],
    ids=['simple json.loads', 'open with encoding', 'encoding in middle']
)
def test_fix_json_loads_encoding(s, expected):
    assert _fix_py3_plus(s) == expected
