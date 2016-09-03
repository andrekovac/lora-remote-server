from flask import Flask, jsonify, make_response, request

from src.twitter import tweet
from src.sensor import get_temperature_celsius

app = Flask(__name__)

# Routes


@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify({'hello': 'world'})


@app.route('/tweet', methods=['GET'])
def send_tweet():
    return jsonify({'tweet': 'not here'})

@app.route('/temperature', methods=['GET'])
def get_temperature():
    temp = get_temperature_celsius()
    return jsonify({'temperature': temp})

# @app.route('/api/v1/submit', methods=['POST'])
# def process_image():
#     jsonData = request.get_json()
#     cutter = ClairesCutter(jsonData['image'], 'base64')
#     positions = cutter.getPositions()
#     pieces = {'red': [], 'green': [], 'blue': []}
#     for color in positions:
#         for position in positions[color]:
#             pieces[color].append(cutter.crop(position))
#
#     return jsonify({'pieces': pieces})


# Pretty error handling
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request. Please check your request syntax.'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Nothing found at this route.'}), 404)


@app.errorhandler(405)
def not_found(error):
    return make_response(jsonify({'error': 'Request method not allowed.'}), 405)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
