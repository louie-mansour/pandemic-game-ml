import pytest
from exceptions.game_end_exceptions import DiseaseCubesDepletedException
from models.board.disease_cube_pool import DiseaseCubePool
from models.shared.colour import Colour

def test_init_sets_max_cubes_for_all_colours():
    pool = DiseaseCubePool()
    assert pool.cubes[Colour.RED] == DiseaseCubePool.MAX_CUBES
    assert pool.cubes[Colour.BLUE] == DiseaseCubePool.MAX_CUBES
    assert pool.cubes[Colour.YELLOW] == DiseaseCubePool.MAX_CUBES
    assert pool.cubes[Colour.BLACK] == DiseaseCubePool.MAX_CUBES

def test_take_cubes_reduces_red_cubes():
    pool = DiseaseCubePool()
    pool.take_cubes(Colour.RED, 5)
    assert pool.cubes[Colour.RED] == DiseaseCubePool.MAX_CUBES - 5

def test_take_cubes_reduces_blue_cubes():
    pool = DiseaseCubePool()
    pool.take_cubes(Colour.BLUE, 3)
    assert pool.cubes[Colour.BLUE] == DiseaseCubePool.MAX_CUBES - 3

def test_take_cubes_reduces_yellow_cubes():
    pool = DiseaseCubePool()
    pool.take_cubes(Colour.YELLOW, 7)
    assert pool.cubes[Colour.YELLOW] == DiseaseCubePool.MAX_CUBES - 7

def test_take_cubes_reduces_black_cubes():
    pool = DiseaseCubePool()
    pool.take_cubes(Colour.BLACK, 10)
    assert pool.cubes[Colour.BLACK] == DiseaseCubePool.MAX_CUBES - 10

def test_take_cubes_returns_false_when_not_enough_red_cubes():
    pool = DiseaseCubePool()
    with pytest.raises(DiseaseCubesDepletedException):
        pool.take_cubes(Colour.RED, DiseaseCubePool.MAX_CUBES + 1)

def test_take_cubes_returns_false_when_not_enough_blue_cubes():
    pool = DiseaseCubePool()
    with pytest.raises(DiseaseCubesDepletedException):
        pool.take_cubes(Colour.BLUE, DiseaseCubePool.MAX_CUBES + 1)

def test_take_cubes_returns_false_when_not_enough_yellow_cubes():
    pool = DiseaseCubePool()
    with pytest.raises(DiseaseCubesDepletedException):
        pool.take_cubes(Colour.YELLOW, DiseaseCubePool.MAX_CUBES + 1)

def test_take_cubes_returns_false_when_not_enough_black_cubes():
    pool = DiseaseCubePool()
    with pytest.raises(DiseaseCubesDepletedException):
        pool.take_cubes(Colour.BLACK, DiseaseCubePool.MAX_CUBES + 1)

def test_take_cubes_multiple_times_reduces_correctly():
    pool = DiseaseCubePool()
    pool.take_cubes(Colour.RED, 5)
    pool.take_cubes(Colour.RED, 3)
    assert pool.cubes[Colour.RED] == DiseaseCubePool.MAX_CUBES - 8

def test_return_cubes_increases_red_cubes():
    pool = DiseaseCubePool()
    pool.take_cubes(Colour.RED, 5)
    pool.return_cubes(Colour.RED, 3)
    assert pool.cubes[Colour.RED] == DiseaseCubePool.MAX_CUBES - 2

def test_return_cubes_increases_blue_cubes():
    pool = DiseaseCubePool()
    pool.take_cubes(Colour.BLUE, 10)
    pool.return_cubes(Colour.BLUE, 5)
    assert pool.cubes[Colour.BLUE] == DiseaseCubePool.MAX_CUBES - 5

def test_return_cubes_increases_yellow_cubes():
    pool = DiseaseCubePool()
    pool.take_cubes(Colour.YELLOW, 8)
    pool.return_cubes(Colour.YELLOW, 8)
    assert pool.cubes[Colour.YELLOW] == DiseaseCubePool.MAX_CUBES

def test_return_cubes_increases_black_cubes():
    pool = DiseaseCubePool()
    pool.take_cubes(Colour.BLACK, 15)
    pool.return_cubes(Colour.BLACK, 10)
    assert pool.cubes[Colour.BLACK] == DiseaseCubePool.MAX_CUBES - 5

def test_return_cubes_raises_exception_when_exceeding_max_red_cubes():
    pool = DiseaseCubePool()
    with pytest.raises(Exception, match="Cannot return more than 24 red cubes to the pool."):
        pool.return_cubes(Colour.RED, 1)

def test_return_cubes_raises_exception_when_exceeding_max_blue_cubes():
    pool = DiseaseCubePool()
    with pytest.raises(Exception, match="Cannot return more than 24 blue cubes to the pool."):
        pool.return_cubes(Colour.BLUE, 1)

def test_return_cubes_raises_exception_when_exceeding_max_yellow_cubes():
    pool = DiseaseCubePool()
    with pytest.raises(Exception, match="Cannot return more than 24 yellow cubes to the pool."):
        pool.return_cubes(Colour.YELLOW, 1)

def test_return_cubes_raises_exception_when_exceeding_max_black_cubes():
    pool = DiseaseCubePool()
    with pytest.raises(Exception, match="Cannot return more than 24 black cubes to the pool."):
        pool.return_cubes(Colour.BLACK, 1)

def test_return_cubes_multiple_times_increases_correctly():
    pool = DiseaseCubePool()
    pool.take_cubes(Colour.BLUE, 10)
    pool.return_cubes(Colour.BLUE, 3)
    pool.return_cubes(Colour.BLUE, 2)
    assert pool.cubes[Colour.BLUE] == DiseaseCubePool.MAX_CUBES - 5
