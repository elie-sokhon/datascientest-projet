from datetime import datetime
from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    pseudonym = db.Column(db.String(80), unique=True, nullable=False)
    connected_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_connected = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<User {self.pseudonym}>"

    def to_dict(self):
        return {
            "id": self.id,
            "pseudonym": self.pseudonym,
            "connected_at": self.connected_at.isoformat(),
            "is_connected": self.is_connected
        }
