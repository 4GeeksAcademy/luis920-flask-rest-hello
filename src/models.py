from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50),)
    hight = db.Column(db.Float, nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    skin_color = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Character {self.first_name} {self.last_name}>'

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "hight": self.hight,
            "gender": self.gender,
            "skin_color": self.skin_color,
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    diameter = db.Column(db.Float, nullable=False)
    climate = db.Column(db.String(50), nullable=False)
    terrain = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Planet {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "climate": self.climate,
            "terrain": self.terrain,
        }

class Specie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    lenguage = db.Column(db.String(50), nullable=False)
    average_height = db.Column(db.Float, nullable=False)
    average_lifespan = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Specie {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lenguage": self.lenguage,
            "average_height": self.average_height,
            "average_lifespan": self.average_lifespan,
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), )
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'),)
    specie_id = db.Column(db.Integer, db.ForeignKey('specie.id'),)

    user = db.relationship('User', backref='favorites')
    character = db.relationship('Character', backref='favorites')
    planet = db.relationship('Planet', backref='favorites')
    specie = db.relationship('Specie', backref='favorites')

    def __repr__(self):
        return f'<Favorites {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "specie_id": self.specie_id,
        }
