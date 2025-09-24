from flask import Blueprint, jsonify, request
from ..composer.user_finder_composer import user_finder_composer
from ..composer.user_creator_composer import user_creator_composer
from ...view.http_types.http_request import HttpRequest

# Define uma rota POST em "/user" dentro do blueprint 'user_routes_bp'
user_routes_bp = Blueprint("user_routes", __name__)

@user_routes_bp.route("/user", methods = ["POST"])
# Uma função para criar usuarios
def regestry_user():
    http_request = HttpRequest(body = request.json)

    user_creator = user_creator_composer()
    http_reponse = user_creator.handle_insert_new_user(http_request)

    # Criou uma rota
    return jsonify(http_reponse.body), http_reponse.status_code


@user_routes_bp.route("/user/find/<person_name>", methods = ["GET"])
def find_user(person_name):
    http_request = HttpRequest(param = {"person_name": person_name})

    user_finder = user_finder_composer()
    http_reponse = user_finder.handle_find_person_by_name(http_request)

    # Criou uma rota
    return jsonify(http_reponse.body), http_reponse.status_code
