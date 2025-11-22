import pytest
from src.models.board import disease_cube_pool
from src.models.map.location import Location, Outbreak, MAX_CUBES_PER_COLOUR
from src.models.board.disease_cube_pool import DiseaseCubePool
from src.models.shared.colour import Colour
from src.models.shared.city import City

@pytest.fixture
def disease_pool():
    return DiseaseCubePool()


@pytest.fixture
def city():
    return City("Atlanta", Colour.BLUE)


@pytest.fixture
def location(city, disease_pool):
    return Location(city=city)


class TestLocationInit:
    def test_location_initialization(self, location, city):
        assert location.city == city
        assert location.cubes == {
            Colour.RED: 0,
            Colour.BLUE: 0,
            Colour.YELLOW: 0,
            Colour.BLACK: 0
        }
        assert len(location.connections) == 0


class TestConnections:
    def test_add_single_connection(self, location, disease_pool):
        other_city = City("Chicago", Colour.BLUE)
        other_location = Location(city=other_city)
        
        location.add_connections(other_location)
        
        assert other_location in location.connections
        assert len(location.connections) == 1

    def test_add_multiple_connections(self, location, disease_pool):
        other_location1 = Location(city=City("Chicago", Colour.BLUE))
        other_location2 = Location(city=City("New York", Colour.BLUE))
        
        location.add_connections(other_location1, other_location2)
        
        assert len(location.connections) == 2
        assert other_location1 in location.connections
        assert other_location2 in location.connections

    def test_connections_property_returns_set(self, location):
        assert isinstance(location.connections, set)


class TestAddCubes:
    def test_add_cubes_within_limit(self, location):
        disease_cube_pool = DiseaseCubePool()
        outbreak = location.add_cubes(disease_cube_pool, 2, Colour.RED)
        
        assert location.cubes[Colour.RED] == 2
        assert outbreak == Outbreak.NONE

    def test_add_cubes_exactly_at_limit(self, location):
        disease_cube_pool = DiseaseCubePool()
        outbreak = location.add_cubes(disease_cube_pool, MAX_CUBES_PER_COLOUR, Colour.BLUE)
        
        assert location.cubes[Colour.BLUE] == MAX_CUBES_PER_COLOUR
        assert outbreak == Outbreak.NONE

    def test_add_cubes_exceeds_limit_triggers_outbreak(self, location):
        disease_cube_pool = DiseaseCubePool()
        outbreak = location.add_cubes(disease_cube_pool, MAX_CUBES_PER_COLOUR + 1, Colour.YELLOW)
        
        assert location.cubes[Colour.YELLOW] == MAX_CUBES_PER_COLOUR
        assert outbreak == Outbreak.YELLOW

    def test_add_cubes_multiple_times_triggers_outbreak(self, location):
        disease_cube_pool = DiseaseCubePool()
        location.add_cubes(disease_cube_pool, 2, Colour.BLACK)
        outbreak = location.add_cubes(disease_cube_pool, 2, Colour.BLACK)
        
        assert location.cubes[Colour.BLACK] == MAX_CUBES_PER_COLOUR
        assert outbreak == Outbreak.BLACK

    def test_add_cubes_invalid_colour_raises_exception(self, location):
        with pytest.raises(Exception, match="Invalid colour specified."):
            location.add_cubes(disease_cube_pool, 1, "invalid_colour")
            
    def test_number_of_cubes_in_disease_pool_after_adding_cubes(self, location, disease_pool):
        disease_cube_pool = DiseaseCubePool()
        initial_red_cubes = disease_cube_pool.cubes[Colour.RED]
        location.add_cubes(disease_cube_pool, 2, Colour.RED)
        assert disease_cube_pool.cubes[Colour.RED] == initial_red_cubes - 2

class TestRemoveCube:
    def test_remove_cube_successfully(self, location):
        disease_cube_pool = DiseaseCubePool()
        location.add_cubes(disease_cube_pool, 2, Colour.RED)
        location.remove_cube(disease_cube_pool, Colour.RED)

        assert location.cubes[Colour.RED] == 1

    def test_remove_cube_when_none_present_raises_exception(self, location):
        disease_cube_pool = DiseaseCubePool()
        with pytest.raises(Exception, match="No red cubes to remove from this location."):
            location.remove_cube(disease_cube_pool, Colour.RED)

    def test_remove_cube_invalid_colour_raises_exception(self, location):
        disease_cube_pool = DiseaseCubePool()
        with pytest.raises(Exception, match="Invalid colour specified."):
            location.remove_cube(disease_cube_pool, "invalid_colour")

    def test_remove_all_cubes(self, location):
        disease_cube_pool = DiseaseCubePool()
        location.add_cubes(disease_cube_pool, 3, Colour.BLUE)
        location.remove_cube(disease_cube_pool, Colour.BLUE)
        location.remove_cube(disease_cube_pool, Colour.BLUE)
        location.remove_cube(disease_cube_pool, Colour.BLUE)

        assert location.cubes[Colour.BLUE] == 0

    def test_number_of_cubes_in_disease_pool_after_removing_cubes(self, location, disease_pool):
        disease_cube_pool = DiseaseCubePool()
        location.add_cubes(disease_cube_pool, 2, Colour.RED)
        initial_red_cubes = disease_cube_pool.cubes[Colour.RED]
        location.remove_cube(disease_cube_pool, Colour.RED)
        assert disease_cube_pool.cubes[Colour.RED] == initial_red_cubes + 1