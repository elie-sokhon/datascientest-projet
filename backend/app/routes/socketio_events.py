from flask_socketio import emit
from app import socketio, db
from app.models.user import User
from app.models.message import Message

@socketio.on('send_message')
def handle_send_message(data):
    """
    Data format expected:
    {
        'sender': 'pseudonym',
        'content': 'your message here'
    }
    """
    sender_name = data.get('sender')
    content = data.get('content')

    if not sender_name or not content:
        emit('error', {'error': 'sender and content required'})
        return

    user = User.query.filter_by(pseudonym=sender_name, is_connected=True).first()
    if not user:
        emit('error', {'error': 'sender not connected'})
        return

    # Save message to database
    message = Message(sender_id=user.id, content=content)
    db.session.add(message)
    db.session.commit()

    # Broadcast message to all connected clients
    emit('receive_message', {
        'sender': sender_name,
        'content': content,
        'timestamp': message.timestamp.isoformat()
    }, broadcast=True)
