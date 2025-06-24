from server.app import app, db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from datetime import date

with app.app_context():
    db.drop_all()
    db.create_all()

    u = User(username="admin", is_admin=True)
    u.set_password("admin")
    db.session.add(u)

    g1 = Guest(name="Beyonce", occupation="Singer")
    g2 = Guest(name="Elon Musk", occupation="Engineer")

    e1 = Episode(date=date(2023, 5, 20), number=101)
    e2 = Episode(date=date(2023, 5, 21), number=102)

    db.session.add_all([g1, g2, e1, e2])
    db.session.commit()

    a1 = Appearance(rating=5, guest=g1, episode=e1)
    a2 = Appearance(rating=4, guest=g2, episode=e2)

    db.session.add_all([a1, a2])
    db.session.commit()
