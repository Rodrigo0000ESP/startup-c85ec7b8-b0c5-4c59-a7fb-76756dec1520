from backend.services import user_service

@app.route('/user', methods=['GET'])
def get_user_data():
    user_data = user_service.get_user_data()
    return jsonify(user_data)

@app.route('/user', methods=['POST'])
def update_user_data():
    request_data = request.get_json()
    updated_data = user_service.update_user_data(request_data)
    return jsonify(updated_data)