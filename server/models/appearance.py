from server.app import db

class Appearance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)

    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'))
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'))

    @staticmethod
    def validate_rating(rating):
        return 1 <= rating <= 5
