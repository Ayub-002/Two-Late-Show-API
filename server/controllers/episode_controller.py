from flask import Blueprint, jsonify, request
from server.app import db
from server.models.episode import Episode
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.models.user import User
from datetime import datetime

episode_bp = Blueprint('episode', __name__, url_prefix='/episodes')

@episode_bp.route("", methods=["GET"])
def get_episodes():
    page = request.args.get("page", 1, type=int)
    per_page = 5
    pagination = Episode.query.paginate(page=page, per_page=per_page, error_out=False)
    episodes = pagination.items
    return {
        "episodes": [
            {"id": e.id, "number": e.number, "date": e.date.isoformat()}
            for e in episodes
        ],
        "total": pagination.total,
        "page": page,
        "pages": pagination.pages
    }

@episode_bp.route("/<int:id>", methods=["GET"])
def get_episode(id):
    e = Episode.query.get_or_404(id)
    return {
        "id": e.id,
        "number": e.number,
        "date": e.date.isoformat(),
        "appearances": [
            {
                "guest": a.guest.name,
                "rating": a.rating
            }
            for a in e.appearances
        ]
    }

@episode_bp.route("/<int:id>", methods=["PATCH"])
def update_episode(id):
    episode = Episode.query.get_or_404(id)
    data = request.get_json()

    if "number" in data:
        episode.number = data["number"]
    if "date" in data:
        episode.date = datetime.strptime(data["date"], "%Y-%m-%d")

    db.session.commit()
    return {
        "id": episode.id,
        "number": episode.number,
        "date": episode.date.isoformat()
    }

@episode_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_episode(id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user or not user.is_admin:
        return {"error": "Admin only"}, 403

    e = Episode.query.get_or_404(id)
    db.session.delete(e)
    db.session.commit()
    return {"message": "Episode deleted"}
