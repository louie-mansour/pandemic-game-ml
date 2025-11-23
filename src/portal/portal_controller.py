from flask import Flask, jsonify
from flask_cors import CORS

from models.board.board import Board

app = Flask(__name__)
CORS(app)


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'ok'})


@app.route('/api/game/board', methods=['GET'])
def get_game_board():
    board = Board()
    return jsonify({
        'locations': {
            str(location.city.value[0]): {
                'colour': str(location.city.colour.value),
                'connections': [str(conn.city.value[0]) for conn in location.connections]
            }
            for location in board.location_graph.locations.values()
        },
        'outbreak_count': board.outbreak_counter.count,
        'infection_rate': board.infection_rate.current_rate
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)