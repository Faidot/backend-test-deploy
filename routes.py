from flask import jsonify, request
from app import app
from models import db, Item

@app.route("/api/items", methods=["GET"])
def get_items():
    items = Item.query.all()
    return jsonify([i.to_dict() for i in items])

@app.route("/api/items", methods=["POST"])
def create_item():
    data = request.json
    item = Item(name=data["name"], description=data.get("description", ""))
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@app.route("/api/items/<int:id>", methods=["PUT"])
def update_item(id):
    item = Item.query.get_or_404(id)
    data = request.json
    item.name = data.get("name", item.name)
    item.description = data.get("description", item.description)
    db.session.commit()
    return jsonify(item.to_dict())

@app.route("/api/items/<int:id>", methods=["DELETE"])
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted"}), 200
