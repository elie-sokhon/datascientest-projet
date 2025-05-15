from datetime import datetime

from app import db
from app.models.user import User
from app.utils.validators import is_valid_pseudonym


class UserService:
    @staticmethod
    def login_user(pseudonym: str):
        # Validate pseudonym rules
        if not is_valid_pseudonym(pseudonym):
            raise ValueError("Invalid pseudonym. Check allowed length and characters.")

        # Check if user already exists
        user = User.query.filter_by(pseudonym=pseudonym).first()
        if user:
            if user.is_connected:
                raise ValueError("User already connected.")
            else:
                # User exists but was disconnected → reconnect
                user.is_connected = True
                user.connected_at = datetime.utcnow()
        else:
            # Create new user
            user = User(pseudonym=pseudonym)
            db.session.add(user)

        db.session.commit()
        return user

    @staticmethod
    def logout_user(pseudonym: str):
        user = User.query.filter_by(pseudonym=pseudonym, is_connected=True).first()
        if not user:
            raise ValueError("User not found or already disconnected.")

        user.is_connected = False
        db.session.commit()
        return True

    @staticmethod
    def list_connected_users(sort_by: str = None):
        query = User.query.filter_by(is_connected=True)

        if sort_by == "pseudonym":
            query = query.order_by(User.pseudonym.asc())
        elif sort_by == "connected_at":
            query = query.order_by(User.connected_at.asc())

        users = query.all()
        return [user.to_dict() for user in users]
