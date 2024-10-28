from flask import jsonify, request
from . import db  # Import db instance
from .models import User

def register_routes(app):
    @app.route('/add_user', methods=['POST'])
    def add_user():
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User added!'}), 201

    @app.route('/users', methods=['GET'])
    def get_users():
        users = User.query.all()
        return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users])

    @app.route('/users/<int:id>', methods=['GET'])
    def get_user(id):
        user = User.query.get(id)  # Fetch user by primary key
        if user:
            return jsonify({'username': user.username, 'email': user.email}), 200
        return jsonify({'message': 'User not found!'}), 404

    @app.route('/users/<int:id>', methods=['PUT'])
    def update_user(id):
        user = User.query.get(id)
        if user:
            data = request.get_json()
            user.username = data.get('username', user.username) 
            user.email = data.get('email', user.email) 
            db.session.commit()
            return jsonify({'message': 'User updated!'}), 200
        return jsonify({'message': 'User not found!'}), 404

    @app.route('/users/<int:id>', methods=['DELETE'])
    def delete_user(id):
        user = User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': 'User deleted!'}), 204
        return jsonify({'message': 'User not found!'}), 404