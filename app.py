from flask import Flask, abort, jsonify, request

app = Flask(__name__)

# Simple in-memory store for demo purposes.
items = {}
next_id = 1


def validate_item_payload(payload, partial=False):
    """Validate incoming JSON payload for create/update."""
    if not isinstance(payload, dict):
        abort(400, description="Request body must be a JSON object")

    if not partial and "name" not in payload:
        abort(400, description="Field 'name' is required")

    if "name" in payload and not isinstance(payload["name"], str):
        abort(400, description="Field 'name' must be a string")

    if "price" in payload and not isinstance(payload["price"], (int, float)):
        abort(400, description="Field 'price' must be a number")


@app.get("/")
def home():
    return jsonify({"message": "Flask CRUD API is running"})


@app.get("/items")
def list_items():
    return jsonify(list(items.values()))


@app.get("/items/<int:item_id>")
def get_item(item_id):
    item = items.get(item_id)
    if item is None:
        abort(404, description="Item not found")
    return jsonify(item)


@app.post("/items")
def create_item():
    global next_id

    data = request.get_json(silent=True)
    validate_item_payload(data, partial=False)

    item = {
        "id": next_id,
        "name": data["name"],
        "price": data.get("price", 0),
    }
    items[next_id] = item
    next_id += 1

    return jsonify(item), 201


@app.put("/items/<int:item_id>")
def update_item(item_id):
    item = items.get(item_id)
    if item is None:
        abort(404, description="Item not found")

    data = request.get_json(silent=True)
    validate_item_payload(data, partial=True)

    if "name" in data:
        item["name"] = data["name"]
    if "price" in data:
        item["price"] = data["price"]

    return jsonify(item)


@app.delete("/items/<int:item_id>")
def delete_item(item_id):
    item = items.pop(item_id, None)
    if item is None:
        abort(404, description="Item not found")
    return "", 204


@app.errorhandler(400)
def handle_bad_request(error):
    return jsonify({"error": "Bad Request", "message": error.description}), 400


@app.errorhandler(404)
def handle_not_found(error):
    return jsonify({"error": "Not Found", "message": error.description}), 404


if __name__ == "__main__":
    app.run(debug=True)
