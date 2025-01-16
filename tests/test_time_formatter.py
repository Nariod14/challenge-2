import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/src')

import pytest
from time_formatter import format_time

def test_format_time():
    assert format_time(90) == "1h 30m"
    assert format_time(45) == "45m"
    assert format_time(120) == "2h"
    assert format_time(150) == "2h 30m"
    assert format_time(0) == "0m"
    
def test_edge_cases():
    with pytest.raises(ValueError):
        format_time(-1)
    with pytest.raises(ValueError):
        format_time("not a number")
    assert format_time(1.5) == "1m"
    assert format_time(1000000) == "16666h 40m"


if __name__ == "__main__":
    test_format_time()
    test_edge_cases()
    # Replace with the actual function name you want to debug