from flask import jsonify

from awtest import app
from awtest.etl import get_all_profiles, get_one_entity, delete_profile


@app.route('/api/v1/resources/profiles/all', methods=['GET'])
def profile_list():
    data = get_all_profiles()
    return jsonify([prof.to_dict() for prof in data] if data else {'message': 'Not found data'})


@app.route('/api/v1/resources/profiles/show/<int:id>', methods=['GET'])
def show_user(id):
    prof = get_one_entity(id)
    return jsonify(prof.to_dict() if prof else {'message': f'Not found profile with index #{id}'})


@app.route('/api/v1/resources/profiles/delete/<int:id>', methods=['DELETE'])
def delete_users(id):
    return jsonify(delete_profile(id))

