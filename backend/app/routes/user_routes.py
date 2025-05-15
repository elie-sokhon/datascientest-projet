from app.services.user_service import UserService
from flask import Blueprint, jsonify, request

user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    pseudonym = data.get("pseudonym")

    if not pseudonym:
        return jsonify({"error": "Pseudonym is required."}), 400

    try:
        user = UserService.login_user(pseudonym)
        return jsonify(user.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@user_bp.route("/logout", methods=["POST"])
def logout():
    data = request.get_json()
    pseudonym = data.get("pseudonym")

    if not pseudonym:
        return jsonify({"error": "Pseudonym is required."}), 400

    try:
        UserService.logout_user(pseudonym)
        return jsonify({"message": f"User '{pseudonym}' has logged out."}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@user_bp.route("/users", methods=["GET"])
def list_users():
    sort_by = request.args.get(
        "sort_by"
    )  # Optional: ?sort_by=pseudonym OR ?sort_by=connected_at
    users = UserService.list_connected_users(sort_by=sort_by)
    return jsonify(users), 200
