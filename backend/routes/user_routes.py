from backend.services import user_service

@user_routes.route('/user_data', methods=['GET'])
def get_user_data():
    data = user_service.retrieve_user_data()
    return data

@user_routes.route('/user_action', methods=['POST'])
def perform_user_action():
    request_data = request.get_json()
    response = user_service.process_user_action(request_data)
    return response