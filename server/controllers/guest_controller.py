from flask import Blueprint, jsonify, request
from server.models.guest import Guest
from server.app import db

guest_bp = Blueprint('guest', __name__, url_prefix='/guests')

@guest_bp.route("", methods=["GET"])
def get_guests():
    page = request.args.get("page", 1, type=int)
    per_page = 5
    pagination = Guest.query.paginate(page=page, per_page=per_page, error_out=False)
    guests = pagination.items
    return {
        "guests": [
            {"id": g.id, "name": g.name, "occupation": g.occupation}
            for g in guests
        ],
        "total": pagination.total,
        "page": page,
        "pages": pagination.pages
    }

@guest_bp.route("/<int:id>", methods=["PATCH"])
def update_guest(id):
    guest = Guest.query.get_or_404(id)
    data = request.get_json()

    if "name" in data:
        guest.name = data["name"]
    if "occupation" in data:
        guest.occupation = data["occupation"]

    db.session.commit()
    return {
        "id": guest.id,
        "name": guest.name,
        "occupation": guest.occupation
    }
