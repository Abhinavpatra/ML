
from flask import Flask, jsonify, request


app = Flask(__name__)

items= [
  {
    "id": 1,
    "name": "Item 1",
    "description": "This is Item 1"
  },
  {
    "id": 2,
    "name": "Item 2",
    "description": "This is Item 2"
  },
  {
    "id": 3,
    "name": "Item 3",
    "description": "This is Item 3"
  }
]


# GET: getting all the users
@app.route("/items", methods = ["GET"])
def get_items():
    return jsonify(items)


# GET: gets specific todos
@app.route("/items/<int:item_id>", methods = ["GET"])
def get_item(item_id):
    item = next((item for item in items if item["id"]==item_id), None)
    if item is None:
        return jsonify({"error":"item is not found"})
    return jsonify(item)


# POST: adding new todo
@app.route("/items", methods=["POST"])
def create_item():
    if not request.json or not "name" in request.json:
        return jsonify({
            "error":"item not found"
        })
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json['name'],
        "description": request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)



# PUT: Editing a pre existing todo
@app.route("/items/<int:item_id>", methods = ["PUT"])
def update_item(item_id):
    item = next((item for item in items if item["id"]==item_id), None)
    if item is None:
        return jsonify({"error":"item is not found"})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description')
    return jsonify(item)

if __name__ == "__main__":
    app.run(debug = True)

