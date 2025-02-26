from collections import namedtuple

STATUS = 'status'
VALUE = 'value'
OLD_VALUE = 'old_value'
NEW_VALUE = 'new_value'

_FORMAT_VALUES = ('stylish', 'plain', 'json')
FORMATS = namedtuple(
    'FormatChoices', map(lambda x: x.upper(), _FORMAT_VALUES)
)(*_FORMAT_VALUES)

_TYPE_VALUES = ('removed', 'added', 'nested', 'updated', 'unchanged')
STATUSES = namedtuple(
    'FormatTypes', map(lambda x: x.upper(), _TYPE_VALUES)
)(*_TYPE_VALUES)

INDENT = '    '
