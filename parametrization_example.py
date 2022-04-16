import pytest
def string_to_bool(s):
    """
    Convert String to Bool
    >>> string_to_bool('True')
    True
    >>> string_to_bool('true')
    True
    >>> string_to_bool('False')
    False
    >>> string_to_bool('false')
    False
    >>> string_to_bool('null')
    >>> string_to_bool(None)
    >>> string_to_bool('')
    """
    if not s:
        return None
    return None if s.lower() == 'null' else s.lower() == 'true'

true_values = ['yes', '1', 'Yes', 'TRUE', 'TruE', 'True', 'true']
class TestStrToBool(object):
    @pytest.mark.parametrize('value', true_values)
    def test_it_detects_truish_strings(self, value):
        assert string_to_bool(value)
