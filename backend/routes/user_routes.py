from backend.services.user_service import fetch_user_data, process_user_data


def get_user_data():
    user_data = fetch_user_data()
    processed_user_data = process_user_data(user_data)
    return processed_user_data