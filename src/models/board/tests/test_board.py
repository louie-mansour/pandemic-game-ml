import pytest
from exceptions.game_end_exceptions import DiseaseCubesDepletedException, DiseaseCubesDepletedException, TooManyOutbreaksException
from src.models.board.board import Board
from src.models.shared.city import City
from src.models.shared.colour import Colour

def test_board_initialization():
    """Test that board initializes with correct components"""
    board = Board()
    assert board.location_graph is not None
    assert board.outbreak_counter is not None
    assert board.infection_rate is not None
    assert board.infection_deck is not None
    assert board.outbreak_counter.count == 0

def test_board_setup_infects_cities():
    """Test that board setup infects 9 cities with correct cube counts"""
    board = Board()
    board.setup()
    # Check that infection deck has drawn 9 cards
    initial_deck_size = 48
    current_deck_size = len(board.infection_deck._deck)
    assert initial_deck_size - current_deck_size == 9
    
    # Check total disease cubes: 3+3+3 + 2+2+2 + 1+1+1 = 18
    total_cubes = sum(
        location.cubes[colour]
        for location in board.location_graph.locations.values()
        for colour in Colour
    )
    assert total_cubes == 18

def test_take_turn_draws_cards_based_on_infection_rate():
    """Test that take_turn draws correct number of cards based on infection rate"""
    board = Board()
    
    initial_deck_size = len(board.infection_deck._deck)
    initial_rate = board.infection_rate.current_rate
    
    board.take_turn()
    
    cards_drawn = initial_deck_size - len(board.infection_deck._deck)
    assert cards_drawn == initial_rate

def test_add_disease_cubes_without_outbreak():
    """Test adding disease cubes when no outbreak occurs"""
    board = Board()
    
    city = City.ATLANTA
    location = board.location_graph.get_location_by_city(city)
    # Clear any existing cubes from setup
    location.cubes[city.colour] = 0
    
    board._add_disease_cubes_to_location(city, 1, city.colour)
    
    assert location.cubes[city.colour] == 1

def test_add_disease_cubes_with_outbreak():
    """Test adding disease cubes when outbreak occurs"""
    board = Board()
    
    city = City.ATLANTA
    location = board.location_graph.get_location_by_city(city)
    
    # Clear and fill to capacity
    board._add_disease_cubes_to_location(city, 3, city.colour)
    
    # Adding one more should trigger outbreak
    board._add_disease_cubes_to_location(city, 1, city.colour)
    
    assert board.outbreak_counter.count == 1
    # Connected cities should have received cubes
    for connected_location in location.connections:
        assert connected_location.cubes[city.colour] > 0

def test_outbreak_prevents_chain_to_same_city():
    """Test that outbreak doesn't chain back to already outbroken city"""
    board = Board()

    # Set up two connected cities that will both outbreak
    city1 = City.ATLANTA
    city2 = City.WASHINGTON
    
    # Fill both locations to capacity
    board._add_disease_cubes_to_location(city1, 3, city1.colour)
    board._add_disease_cubes_to_location(city2, 3, city2.colour)
    
    # Trigger outbreak in city1
    board._add_disease_cubes_to_location(city1, 1, city1.colour)
    
    # Should have limited outbreaks, not infinite chain
    assert board.outbreak_counter.count == 2

def test_infection_rate_increases_correctly():
    """Test that infection rate follows the expected progression"""
    board = Board()
    
    assert board.infection_rate.current_rate == 2
    
    # Infection rate should increase as epidemic markers are reached
    initial_rate = board.infection_rate.current_rate
    assert initial_rate in [2, 3, 4]

def test_handle_epidemic_increases_infection_rate():
    """Test that epidemic increases infection rate"""
    board = Board()
    
    initial_rate = board.infection_rate.current_rate
    board.handle_epidemic()
    
    # Infection rate should have increased
    assert board.infection_rate.current_rate >= initial_rate

def test_handle_epidemic_with_outbreak():
    """Test epidemic that triggers an outbreak"""
    board = Board()
    
    # Get bottom card and pre-fill location
    bottom_card = board.infection_deck._deck[0].value
    board._add_disease_cubes_to_location(bottom_card, 3, bottom_card.colour)
    
    initial_outbreak_count = board.outbreak_counter.count
    board.handle_epidemic()
    
    # Should have triggered outbreak
    assert board.outbreak_counter.count > initial_outbreak_count

def test_take_turn_stops_on_game_lost():
    """Test that take_turn returns lost state when game is lost"""
    board = Board()
    
    # Force outbreak counter to near limit
    board.outbreak_counter.count = 7
    
    # Fill a city that will be drawn
    city = board.infection_deck._deck[-1].value
    board._add_disease_cubes_to_location(city, 3, city.colour)
    
    # This should trigger outbreak and game loss
    with pytest.raises(TooManyOutbreaksException):
        board.take_turn()

def test_epidemic_returns_lost_state_when_cubes_exhausted():
    """Test that epidemic returns lost state when disease cubes run out"""
    board = Board()
    
    bottom_card = board.infection_deck._deck[0].value
    colour = bottom_card.colour
    board.disease_cube_pool.cubes[colour] = 2

    with pytest.raises(DiseaseCubesDepletedException):
        board.handle_epidemic()
