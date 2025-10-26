import unittest
import pytest
from src.models.board.outbreak_counter import OutbreakCounter, MAX_OUTBREAKS


class TestOutbreakCounter(unittest.TestCase):
    def test_outbreak_counter_starts_at_zero(self):
        counter = OutbreakCounter()
        assert counter.count == 0

    def test_increment_increases_count(self):
        counter = OutbreakCounter()
        counter.increment()
        assert counter.count == 1

    def test_multiple_increments(self):
        counter = OutbreakCounter()
        for _ in range(3):
            counter.increment()
        assert counter.count == 3

    def test_raises_exception_at_max_outbreaks(self):
        counter = OutbreakCounter()
        for _ in range(MAX_OUTBREAKS):
            counter.increment()
        with pytest.raises(Exception) as excinfo:
            counter.increment()
        assert str(excinfo.value) == "Maximum number of outbreaks reached."

    def test_count_at_max_outbreaks(self):
        counter = OutbreakCounter()
        for _ in range(MAX_OUTBREAKS):
            counter.increment()
        self.assertEqual(counter.count, MAX_OUTBREAKS)

if __name__ == "__main__":
    unittest.main()

    