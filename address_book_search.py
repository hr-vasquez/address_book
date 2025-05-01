from flask import Flask, request, jsonify

from search_decorator import search_decorator

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    name = request.args.get('name')
    phone_number = request.args.get('phone_number')
    address = request.args.get('address')
    search_type = request.args.get('search_type')

    if not search_type:
        return jsonify({"error": "search_type is required"}), 400

    if not name and not phone_number and not address:
        return jsonify({"error": "Missing search term. It could be the name, address or phone_number"}), 400

    search_strategy = search_decorator.get_search_algorithms().get(search_type)
    if not search_strategy:
        return jsonify({"error": "Invalid search_type value"}), 400

    result = []
    if name:
        result = search_strategy().search_name(name)
    elif phone_number:
        result = search_strategy().search_phone_number(phone_number)
    elif address:
        result = search_strategy().search_address(address)

    if not result:
        return jsonify({"message": "Record not found"}), 404

    return jsonify([c.to_dict() for c in result])

if __name__ == '__main__':
    app.run(debug=True)
