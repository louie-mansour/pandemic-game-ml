import pytest
from src.models.board.infection_rate import InfectionRate

def test_initial_rate():
    infection_rate = InfectionRate()
    assert infection_rate.current_rate == 2

def test_increase_rate():
    infection_rate = InfectionRate()
    infection_rate.increase()
    assert infection_rate.current_rate == 2
    infection_rate.increase()
    assert infection_rate.current_rate == 2
    infection_rate.increase()
    assert infection_rate.current_rate == 3
    infection_rate.increase()
    assert infection_rate.current_rate == 3
    infection_rate.increase()
    assert infection_rate.current_rate == 4
    infection_rate.increase()
    assert infection_rate.current_rate == 4

    # Check that increasing after maximum rate does not change the rate
    infection_rate.increase()
    assert infection_rate.current_rate == 4