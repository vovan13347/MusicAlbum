from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rock_albums.db'
db = SQLAlchemy(app)

class RockAlbum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    band = db.Column(db.String(120), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'band': self.band
        }
    
def create_app_context():
    with app.app_context():
        db.create_all()

@app.route('/albums', methods=['GET'])
def get_albums():
    albums = RockAlbum.query.all()
    return jsonify([album.to_dict() for album in albums])

@app.route('/albums/<int:id>', methods=['GET'])
def get_album(id):
    album = RockAlbum.query.get_or_404(id)
    return jsonify(album.to_dict())

@app.route('/albums', methods=['POST'])
def add_album():
    data = request.get_json()
    new_album = RockAlbum(title=data['title'], band=data['band'])
    db.session.add(new_album)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Album with this title already exists'}), 400
    return jsonify(new_album.to_dict()), 201

@app.route('/albums/<int:id>', methods=['PUT'])
def update_album(id):
    album = RockAlbum.query.get_or_404(id)
    data = request.get_json()
    album.title = data['title']
    album.band = data['band']
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Album with this title already exists'}), 400
    return jsonify(album.to_dict())

@app.route('/albums/<int:id>', methods=['DELETE'])
def delete_album(id):
    album = RockAlbum.query.get_or_404(id)
    db.session.delete(album)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)