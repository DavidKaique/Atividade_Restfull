from flask_restful import Resource
from models import db, Tutor, Pet

class TutorResource(Resource):
    def get (self, tutor_id):
        tutor = Tutor.query.get(tutor_id)
        return tutor

class PetResource (Resource):
    def get (self, pet_id):
        pet = Pet.query.get(pet_id)
        return pet
        