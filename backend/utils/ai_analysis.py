from data_aggregation import load_data
from preprocessing import preprocess_data
from ai_algorithms import apply_ai


def generate_insights():
    data = load_data()
    preprocessed_data = preprocess_data(data)
    insights = apply_ai(preprocessed_data)
    return insights