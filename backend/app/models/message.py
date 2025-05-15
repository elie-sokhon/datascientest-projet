from datetime import datetime

from app import db

from .user import User  # relative import to avoid future circular problems


class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    sender = db.relationship("User", backref=db.backref("messages", lazy=True))

    def __repr__(self):
        return f"<Message from User {self.sender_id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "sender_id": self.sender_id,
            "sender_name": self.sender.pseudonym if self.sender else None,
            "content": self.content,
            "timestamp": self.timestamp.isoformat(),
        }
