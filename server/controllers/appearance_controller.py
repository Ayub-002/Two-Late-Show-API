from flask import Blueprint, request
from server.app import db
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.models.episode import Episode
from flask_jwt_extended import jwt_required

appearance_bp = Blueprint('appearance', __name__, url_prefix='/appearances')

@appearance_bp.route("", methods=["POST"])
@jwt_required()
def create_appearance():
    data = request.get_json()

    guest = Guest.query.get(data.get("guest_id"))
    episode = Episode.query.get(data.get("episode_id"))
    rating = data.get("rating")

    if not guest or not episode:
        return {"error": "Invalid guest_id or episode_id"}, 400

    if not Appearance.validate_rating(rating):
        return {"error": "Rating must be between 1 and 5"}, 400

    appearance = Appearance(
        guest_id=guest.id,
        episode_id=episode.id,
        rating=rating
    )
    db.session.add(appearance)
    db.session.commit()

    return {"message": "Appearance created"}, 201
