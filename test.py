import pytest
from graph import align_string



def test_align_string_with_multiple_words():
    result = align_string("This is a test", 20)
    assert result == "This   is   a   test"

def test_align_string_short_width():
    result = align_string("This is a test", 10)
    assert result == "This is a test"

def test_align_string_extra_spaces():
    result = align_string("  Hello   world ", 15)
    assert result == "  Hello   world"

if __name__ == "__main__":
    pytest.main()
