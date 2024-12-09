"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os,json
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User , Character ,Planet , Specie
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Obtener todos los usuarios
@app.route('/user', methods=['GET'])
def get_all_users():
    try:
       users = User.query.all()
       if len(users) < 1:
           return jsonify({"msg": "Not Found"}),404
       serialized_users = list(map(lambda x: x.serialize(),users))
       return serialized_users,200
    except Exception as e:
        return jsonify({"msg": "Server Error" , "error": str(e)}),500


# Obtener un usuario
@app.route('/User/int:user_id', methods=['GET'])
def get_user(user_id):
    try:
       user = User.query.get(user_id)
       if user is None:
           return jsonify({"msg": f"user {user_id} not found" }),404
       serialized_user = user.serialize()
       return serialized_user,200
    except Exception as e:
        return jsonify({"msg": "Server Error" , "error": str(e)}),500 

# Crear  un usuario
@app.route('/user', methods=['POST'])
def create_user():
    try:
       body = json.loads(request.data)
       new_user= User(
           email = body["email"] ,
           password = body["password"],
           is_active = True
           
       )
       db.session.add(new_user)
       db.session.commit()
       return jsonify({"msg": "User created succesfull" }),200
    except Exception as e:
        return jsonify({"msg": "Server Error" , "error": str(e)}),500 


# Obtener todos los personajes
@app.route('/character', methods=['GET'])
def get_all_characters():
    try:
       characters = Character.query.all()
       if len(characters) < 1:
           return jsonify({"msg": "Not Found"}),404
       serialized_characters = list(map(lambda x: x.serialize(),characters))
       return serialized_characters,200
    except Exception as e:
        return jsonify({"msg": "Server Error" , "error": str(e)}),500


# Obtener un personaje
@app.route('/character/int:character_id', methods=['GET'])
def get_character(character_id):
    try:
       character = Character.query.get(character_id)
       if character is None:
           return jsonify({"msg": f"user {character_id} not found" }),404
       serialized_character = character.serialize()
       return serialized_character,200
    except Exception as e:
        return jsonify({"msg": "Server Error" , "error": str(e)}),500 

# Crear  un personaje
@app.route('/character', methods=['POST'])
def create_character():
    try:
       body = json.loads(request.data)
       new_character= Character(
           first_name = body["first_name"] ,
           last_name = body["last_name"],
           hight = body["hight"],
           gender = body["gender"] ,
           skin_color = body["skin_color"]
       )
       db.session.add(new_character)
       db.session.commit()
       return jsonify({"msg": "Character created succesfull" }),200
    except Exception as e:
        return jsonify({"msg": "Server Error" , "error": str(e)}),500 
    
    # Obtener todos los planetas
@app.route('/planet', methods=['GET'])
def get_all_planets():
    try:
       planets = Planet.query.all()
       if len(planets) < 1:
           return jsonify({"msg": "Not Found"}),404
       serialized_planets = list(map(lambda x: x.serialize(),planets))
       return serialized_planets,200
    except Exception as e:
        return jsonify({"msg": "Server Error" , "error": str(e)}),500


# Obtener un planeta
@app.route('/planet/int:planet_id', methods=['GET'])
def get_planet(planet_id):
    try:
       planet = Planet.query.get(planet_id)
       if planet is None:
           return jsonify({"msg": f"user {planet_id} not found" }),404
       serialized_planet = planet.serialize()
       return serialized_planet,200
    except Exception as e:
        return jsonify({"msg": "Server Error" , "error": str(e)}),500 

# Crear  un planeta
@app.route('/planet', methods=['POST'])
def create_planet():
    try:
       body = json.loads(request.data)
       new_planet= Planet(
           name = body["name"] ,
           diameter = body["diameter"],
           climate = body["climate"],
           terrain = body["terrain"]
           
       )
       db.session.add(new_planet)
       db.session.commit()
       return jsonify({"msg": "Character created succesfull" }),200
    except Exception as e:
        return jsonify({"msg": "Server Error" , "error": str(e)}),500 
    

    # Obtener todas las especies
@app.route('/specie', methods=['GET'])
def get_all_species():
    try:
       species = Specie.query.all()
       if len(species) < 1:
           return jsonify({"msg": "Not Found"}),404
       serialized_species = list(map(lambda x: x.serialize(),species))
       return serialized_species,200
    except Exception as e:
        return jsonify({"msg": "Server Error" , "error": str(e)}),500


# Obtener una especie
@app.route('/specie/int:specie_id', methods=['GET'])
def get_specie(specie_id):
    try:
       specie = Specie.query.get(specie_id)
       if specie is None:
           return jsonify({"msg": f"user {specie_id} not found" }),404
       serialized_specie = specie.serialize()
       return serialized_specie,200
    except Exception as e:
        return jsonify({"msg": "Server Error" , "error": str(e)}),500 

# Crear  una specie
@app.route('/specie', methods=['POST'])
def create_specie():
    try:
       body = json.loads(request.data)
       new_specie= Specie(
           name = body["name"] ,
           lenguage = body["lenguage"],
           average_height = body["average_height"],
           average_lifespan = body["average_lifespan"]
           
       )
       db.session.add(new_specie)
       db.session.commit()
       return jsonify({"msg": "Specie created succesfull" }),200
    except Exception as e:
        return jsonify({"msg": "Server Error" , "error": str(e)}),500 
    

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
